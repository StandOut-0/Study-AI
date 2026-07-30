"""
Qwen2.5-0.5B-Instruct 모델에 한국어 고객 상담 데이터를 학습시키는
4bit QLoRA 기반 Supervised Fine-Tuning 전체 코드입니다.
"""

# 사용하지 않는 객체와 GPU 캐시를 정리하기 위해 gc를 사용합니다.
import gc

# 학습 설정과 결과를 JSON 파일로 저장하기 위해 사용합니다.
import json

# .env 환경변수를 읽기 위해 사용합니다.
import os

# 파일 및 디렉터리 경로를 운영체제 독립적으로 처리합니다.
from pathlib import Path

# 다양한 반환 자료형을 타입 힌트로 표시하기 위해 사용합니다.
from typing import Any

# 모델 학습, GPU 연산 및 추론을 수행하는 PyTorch입니다.
import torch

# Hugging Face JSON 데이터셋을 불러옵니다.
from datasets import load_dataset

# .env 파일의 환경변수를 현재 프로세스에 로드합니다.
from dotenv import load_dotenv

# LoRA 설정과 양자화 모델의 학습 준비 기능을 가져옵니다.
from peft import LoraConfig, prepare_model_for_kbit_training

# 모델, Tokenizer, 양자화 설정 및 난수 시드 함수를 가져옵니다.
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    set_seed,
)

# SFT 전용 Trainer와 학습 설정 클래스를 가져옵니다.
from trl import SFTConfig, SFTTrainer


# 현재 파일의 폴더를 프로젝트 기준 경로로 지정합니다.
BASE_DIR = Path(__file__).resolve().parent

# 프로젝트 루트의 .env 파일을 로드합니다.
load_dotenv(BASE_DIR / ".env")

# 학습 데이터 경로를 지정합니다.
TRAIN_FILE = BASE_DIR / "data" / "train.jsonl"

# 검증 데이터 경로를 지정합니다.
VALID_FILE = BASE_DIR / "data" / "valid.jsonl"

# 환경변수 값이 없을 때 사용할 기본 모델을 지정합니다.
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-0.5B-Instruct")

# LoRA Adapter의 최종 저장 경로를 지정합니다.
OUTPUT_DIR = BASE_DIR / os.getenv(
    "OUTPUT_DIR",
    "outputs/qwen2.5-korean-sft-lora",
)

# Trainer 체크포인트 저장 경로를 지정합니다.
CHECKPOINT_DIR = BASE_DIR / "outputs" / "checkpoints"

# 비공개 모델 또는 승인형 모델 접근에 사용할 Hugging Face 토큰을 읽습니다.
HF_TOKEN = os.getenv("HF_TOKEN") or None

# 반복 실행 시 가능한 범위에서 동일한 결과를 얻기 위한 난수 시드입니다.
SEED = 42

# 한 샘플에 허용할 최대 토큰 길이입니다.
MAX_LENGTH = 512

# GPU 한 장당 실제 학습 배치 크기입니다.
TRAIN_BATCH_SIZE = 1

# GPU 한 장당 검증 배치 크기입니다.
EVAL_BATCH_SIZE = 1

# 지정된 횟수만큼 Gradient를 누적한 뒤 파라미터를 한 번 갱신합니다.
GRADIENT_ACCUMULATION_STEPS = 8

# 전체 학습 데이터 반복 횟수입니다.
NUM_TRAIN_EPOCHS = 3

# LoRA 파라미터를 갱신할 학습률입니다.
LEARNING_RATE = 2e-4

# 모델 가중치가 과도하게 커지는 것을 완화하는 규제 계수입니다.
WEIGHT_DECAY = 0.01

# 전체 학습 Step 중 학습률을 점진적으로 증가시킬 비율입니다.
WARMUP_RATIO = 0.05

# 학습 로그를 출력할 Step 간격입니다.
LOGGING_STEPS = 1

# 저장할 최대 체크포인트 개수입니다.
SAVE_TOTAL_LIMIT = 2


def print_environment() -> None:
    """
    PyTorch, CUDA 및 GPU 정보를 출력합니다.
    """

    # 실행 환경 확인 영역의 제목을 출력합니다.
    print("=" * 80)
    print("1. 실행 환경 확인")
    print("=" * 80)

    # 현재 설치된 PyTorch 버전을 출력합니다.
    print(f"PyTorch 버전       : {torch.__version__}")

    # PyTorch에서 CUDA를 사용할 수 있는지 출력합니다.
    print(f"CUDA 사용 가능     : {torch.cuda.is_available()}")

    # CUDA GPU가 있는 경우 상세 정보를 출력합니다.
    if torch.cuda.is_available():
        # 사용 가능한 GPU 개수를 출력합니다.
        print(f"GPU 개수            : {torch.cuda.device_count()}")

        # 첫 번째 GPU의 제품명을 출력합니다.
        print(f"GPU 이름            : {torch.cuda.get_device_name(0)}")

        # 현재 PyTorch 빌드가 사용하는 CUDA 버전을 출력합니다.
        print(f"PyTorch CUDA 버전   : {torch.version.cuda}")

        # GPU 전체 메모리를 Byte에서 GB로 변환합니다.
        total_memory_gb = torch.cuda.get_device_properties(0).total_memory / 1024**3

        # 변환된 GPU 메모리를 출력합니다.
        print(f"GPU 전체 메모리     : {total_memory_gb:.2f} GB")
    else:
        # CUDA가 없으면 4bit QLoRA 학습이 정상적으로 실행되기 어렵다는 사실을 알립니다.
        print("경고: CUDA GPU가 없습니다. NVIDIA GPU 환경에서 실행하세요.")


def validate_files() -> None:
    """
    학습에 필요한 데이터 파일의 존재 여부를 검사합니다.
    """

    # train.jsonl이 없으면 데이터 생성 코드를 먼저 실행하도록 오류를 발생시킵니다.
    if not TRAIN_FILE.exists():
        raise FileNotFoundError(
            f"학습 데이터가 없습니다: {TRAIN_FILE}\n"
            "먼저 python 01_create_dataset.py를 실행하세요."
        )

    # valid.jsonl이 없으면 데이터 생성 코드를 먼저 실행하도록 오류를 발생시킵니다.
    if not VALID_FILE.exists():
        raise FileNotFoundError(
            f"검증 데이터가 없습니다: {VALID_FILE}\n"
            "먼저 python 01_create_dataset.py를 실행하세요."
        )


def load_sft_datasets():
    """
    JSONL 학습/검증 파일을 Hugging Face Dataset 객체로 불러옵니다.
    """

    # 데이터 분할 이름과 실제 파일 경로를 연결합니다.
    data_files = {
        "train": str(TRAIN_FILE),
        "validation": str(VALID_FILE),
    }

    # JSONL 파일을 DatasetDict 형식으로 불러옵니다.
    dataset_dict = load_dataset("json", data_files=data_files)

    # 학습 분할을 가져옵니다.
    train_dataset = dataset_dict["train"]

    # 검증 분할을 가져옵니다.
    valid_dataset = dataset_dict["validation"]

    # 데이터셋 로드 결과를 출력합니다.
    print("\n" + "=" * 80)
    print("2. 데이터셋 로드")
    print("=" * 80)
    print(f"학습 데이터 수 : {len(train_dataset)}")
    print(f"검증 데이터 수 : {len(valid_dataset)}")
    print(f"데이터 컬럼     : {train_dataset.column_names}")

    # 첫 번째 샘플을 들여쓰기된 JSON 형태로 출력합니다.
    print("\n첫 번째 학습 데이터:")
    print(json.dumps(train_dataset[0], ensure_ascii=False, indent=2))

    # 두 데이터셋을 호출한 쪽으로 반환합니다.
    return train_dataset, valid_dataset


def select_compute_dtype() -> torch.dtype:
    """
    GPU가 BF16을 지원하면 bfloat16, 그렇지 않으면 float16을 선택합니다.
    """

    # CUDA GPU가 존재하고 BF16을 지원하는지 확인합니다.
    if torch.cuda.is_available() and torch.cuda.is_bf16_supported():
        # BF16은 넓은 표현 범위를 제공하여 학습 안정성에 유리할 수 있습니다.
        return torch.bfloat16

    # BF16을 사용할 수 없는 GPU에서는 FP16을 사용합니다.
    return torch.float16


def load_tokenizer():
    """
    기본 모델의 Tokenizer를 불러오고 Padding 설정을 적용합니다.
    """

    # Tokenizer 로드 단계의 제목과 모델 이름을 출력합니다.
    print("\n" + "=" * 80)
    print("3. Tokenizer 로드")
    print("=" * 80)
    print(f"Tokenizer 모델 : {MODEL_NAME}")

    # Hugging Face Hub에서 모델에 대응하는 Tokenizer를 다운로드합니다.
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True,
        token=HF_TOKEN,
    )

    # 일부 모델에 Padding Token이 없을 경우 EOS Token을 대신 사용합니다.
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Causal LM 학습에 적합하도록 오른쪽 Padding을 적용합니다.
    tokenizer.padding_side = "right"

    # 적용된 특수 토큰 정보를 출력합니다.
    print(f"PAD Token          : {tokenizer.pad_token}")
    print(f"PAD Token ID       : {tokenizer.pad_token_id}")
    print(f"EOS Token          : {tokenizer.eos_token}")
    print(f"EOS Token ID       : {tokenizer.eos_token_id}")

    # 설정이 완료된 Tokenizer를 반환합니다.
    return tokenizer


def create_quantization_config(compute_dtype: torch.dtype) -> BitsAndBytesConfig:
    """
    4bit NF4 QLoRA 양자화 설정을 생성합니다.
    """

    # BitsAndBytesConfig 객체에 4bit 양자화 방식을 지정합니다.
    return BitsAndBytesConfig(
        # 모델 가중치를 4bit로 불러와 GPU 메모리 사용량을 줄입니다.
        load_in_4bit=True,

        # QLoRA에서 널리 사용하는 NF4 양자화 형식을 지정합니다.
        bnb_4bit_quant_type="nf4",

        # 양자화 상수를 다시 양자화하여 추가 메모리를 절약합니다.
        bnb_4bit_use_double_quant=True,

        # 실제 행렬 연산은 BF16 또는 FP16으로 수행합니다.
        bnb_4bit_compute_dtype=compute_dtype,
    )


def load_quantized_model(tokenizer, compute_dtype: torch.dtype):
    """
    기본 모델을 4bit로 불러오고 k-bit LoRA 학습이 가능하도록 준비합니다.
    """

    # 모델 로드 단계의 정보를 출력합니다.
    print("\n" + "=" * 80)
    print("4. 4bit 사전 학습 모델 로드")
    print("=" * 80)
    print(f"모델 이름          : {MODEL_NAME}")
    print(f"계산 데이터 타입   : {compute_dtype}")

    # 4bit 양자화 설정을 생성합니다.
    quantization_config = create_quantization_config(compute_dtype)

    # Causal Language Model을 4bit 상태로 첫 번째 GPU에 불러옵니다.
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        quantization_config=quantization_config,
        device_map={"": 0},
        trust_remote_code=True,
        token=HF_TOKEN,
    )

    # 모델의 Padding Token ID를 Tokenizer와 동일하게 맞춥니다.
    model.config.pad_token_id = tokenizer.pad_token_id

    # Gradient Checkpointing과 충돌할 수 있으므로 학습 중 캐시를 비활성화합니다.
    model.config.use_cache = False

    # 양자화된 모델을 k-bit 학습이 가능한 상태로 변환합니다.
    model = prepare_model_for_kbit_training(
        model,
        use_gradient_checkpointing=True,
    )

    # 중간 활성값을 다시 계산하는 방식으로 GPU 메모리를 절약합니다.
    model.gradient_checkpointing_enable()

    # 학습 준비가 완료된 모델을 반환합니다.
    return model


def create_lora_config() -> LoraConfig:
    """
    Qwen 계열 모델의 Attention과 MLP Projection Layer에 적용할 LoRA 설정을 생성합니다.
    """

    # LoRA 설정 단계의 제목을 출력합니다.
    print("\n" + "=" * 80)
    print("5. LoRA 설정")
    print("=" * 80)

    # LoRA Adapter 구성 정보를 정의합니다.
    lora_config = LoraConfig(
        # 저차원 행렬의 Rank입니다.
        r=16,

        # LoRA 출력에 적용하는 Scaling 계수입니다.
        lora_alpha=32,

        # LoRA 경로에 적용할 Dropout 비율입니다.
        lora_dropout=0.05,

        # 원본 Linear Layer의 Bias는 학습하지 않습니다.
        bias="none",

        # 다음 토큰 예측형 언어 모델 작업임을 지정합니다.
        task_type="CAUSAL_LM",

        # LoRA를 적용할 Qwen 내부 Linear Layer 이름입니다.
        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            "gate_proj",
            "up_proj",
            "down_proj",
        ],
    )

    # 주요 LoRA 설정값을 출력합니다.
    print(f"LoRA Rank          : {lora_config.r}")
    print(f"LoRA Alpha         : {lora_config.lora_alpha}")
    print(f"LoRA Dropout       : {lora_config.lora_dropout}")
    print(f"Target Modules     : {lora_config.target_modules}")

    # 완성된 LoRA 설정을 반환합니다.
    return lora_config


def create_training_config(compute_dtype: torch.dtype) -> SFTConfig:
    """
    SFTTrainer가 사용할 전체 학습 설정을 생성합니다.
    """

    # 현재 연산 타입이 BF16인지 확인합니다.
    use_bf16 = compute_dtype == torch.bfloat16

    # 현재 연산 타입이 FP16인지 확인합니다.
    use_fp16 = compute_dtype == torch.float16

    # 최종 Adapter 저장 폴더를 생성합니다.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 체크포인트 저장 폴더를 생성합니다.
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)

    # SFT 전용 학습 설정을 생성합니다.
    return SFTConfig(
        # 체크포인트와 Trainer 상태를 저장할 폴더입니다.
        output_dir=str(CHECKPOINT_DIR),

        # 전체 데이터 반복 횟수입니다.
        num_train_epochs=NUM_TRAIN_EPOCHS,

        # GPU 한 장당 학습 배치 크기입니다.
        per_device_train_batch_size=TRAIN_BATCH_SIZE,

        # GPU 한 장당 검증 배치 크기입니다.
        per_device_eval_batch_size=EVAL_BATCH_SIZE,

        # Gradient 누적 횟수입니다.
        gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,

        # LoRA 파라미터 학습률입니다.
        learning_rate=LEARNING_RATE,

        # Weight Decay 규제 계수입니다.
        weight_decay=WEIGHT_DECAY,

        # Warm-up 비율입니다.
        warmup_ratio=WARMUP_RATIO,

        # Cosine 방식으로 학습률을 감소시킵니다.
        lr_scheduler_type="cosine",

        # 메모리 효율적인 8bit Paged AdamW Optimizer를 사용합니다.
        optim="paged_adamw_8bit",

        # 지정된 Step 간격마다 Loss 등을 출력합니다.
        logging_steps=LOGGING_STEPS,

        # 첫 Step부터 로그를 기록합니다.
        logging_first_step=True,

        # Epoch마다 검증 데이터 평가를 수행합니다.
        eval_strategy="epoch",

        # Epoch마다 체크포인트를 저장합니다.
        save_strategy="epoch",

        # 체크포인트를 최대 두 개까지만 유지합니다.
        save_total_limit=SAVE_TOTAL_LIMIT,

        # 학습 종료 시 eval_loss가 가장 낮은 모델을 복원합니다.
        load_best_model_at_end=True,

        # 최적 모델 판단 지표로 eval_loss를 사용합니다.
        metric_for_best_model="eval_loss",

        # eval_loss는 낮을수록 좋으므로 False로 지정합니다.
        greater_is_better=False,

        # GPU가 BF16을 지원할 때 BF16 혼합 정밀도를 사용합니다.
        bf16=use_bf16,

        # BF16 미지원 GPU에서는 FP16 혼합 정밀도를 사용합니다.
        fp16=use_fp16,

        # GPU 메모리를 줄이기 위해 Gradient Checkpointing을 사용합니다.
        gradient_checkpointing=True,

        # 최신 PyTorch 권장 방식인 비재진입 체크포인팅을 사용합니다.
        gradient_checkpointing_kwargs={"use_reentrant": False},

        # 한 학습 샘플의 최대 Token 길이입니다.
        max_length=MAX_LENGTH,

        # 여러 샘플을 한 시퀀스에 채워 넣는 Packing은 실습 이해를 위해 끕니다.
        packing=False,

        # TensorBoard 형식으로 로그를 저장합니다.
        report_to=["tensorboard"],

        # 데이터 전처리에 사용할 프로세스 수입니다.
        dataset_num_proc=1,

        # messages 컬럼이 자동 제거되지 않도록 합니다.
        remove_unused_columns=False,

        # 모델 학습 난수 시드입니다.
        seed=SEED,

        # 데이터 샘플링 난수 시드입니다.
        data_seed=SEED,
    )


def count_parameters(model) -> dict[str, Any]:
    """
    전체 파라미터와 실제 학습 가능한 파라미터 수 및 비율을 계산합니다.
    """

    # 전체 파라미터 개수 누적 변수입니다.
    total_parameters = 0

    # requires_grad=True인 파라미터 개수 누적 변수입니다.
    trainable_parameters = 0

    # 모델의 모든 파라미터 Tensor를 순회합니다.
    for parameter in model.parameters():
        # 현재 Tensor의 원소 수를 전체 파라미터에 더합니다.
        total_parameters += parameter.numel()

        # Gradient 계산 대상일 때만 학습 가능 파라미터에 더합니다.
        if parameter.requires_grad:
            trainable_parameters += parameter.numel()

    # 전체 대비 학습 가능 파라미터 비율을 계산합니다.
    trainable_ratio = (
        100 * trainable_parameters / total_parameters
        if total_parameters > 0
        else 0.0
    )

    # 계산 결과를 딕셔너리로 반환합니다.
    return {
        "total_parameters": total_parameters,
        "trainable_parameters": trainable_parameters,
        "trainable_ratio": trainable_ratio,
    }


def save_json(data: Any, file_path: Path) -> None:
    """
    학습 설정이나 결과를 UTF-8 JSON 파일로 저장합니다.
    """

    # 대상 파일의 부모 폴더가 없으면 생성합니다.
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # UTF-8 쓰기 모드로 파일을 엽니다.
    with file_path.open("w", encoding="utf-8") as file:
        # Tensor 등 직접 변환되지 않는 값은 문자열로 변환해 저장합니다.
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2,
            default=str,
        )


def run_test_inference(model, tokenizer, question: str) -> str:
    """
    현재 학습된 모델로 한 개의 테스트 질문에 대한 답변을 생성합니다.
    """

    # 추론 속도 향상을 위해 KV Cache를 다시 활성화합니다.
    model.config.use_cache = True

    # Dropout 등을 비활성화하도록 모델을 평가 모드로 변경합니다.
    model.eval()

    # 모델에 전달할 system/user 대화를 구성합니다.
    messages = [
        {
            "role": "system",
            "content": (
                "당신은 온라인 쇼핑몰의 고객 상담 AI입니다. "
                "고객의 질문에 친절하고 정확하게 답변하세요."
            ),
        },
        {
            "role": "user",
            "content": question,
        },
    ]

    # 모델의 Chat Template을 적용해 문자열 프롬프트를 생성합니다.
    prompt_text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    # 문자열 프롬프트를 PyTorch Tensor로 Tokenizing합니다.
    inputs = tokenizer(prompt_text, return_tensors="pt")

    # 모든 입력 Tensor를 모델이 위치한 GPU로 이동합니다.
    inputs = {
        key: value.to(model.device)
        for key, value in inputs.items()
    }

    # Gradient를 계산하지 않는 추론 전용 모드로 실행합니다.
    with torch.inference_mode():
        # 모델이 새로운 답변 토큰을 생성합니다.
        generated_ids = model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.1,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )

    # 입력 프롬프트 토큰을 제외한 신규 생성 토큰만 선택합니다.
    new_tokens = generated_ids[:, inputs["input_ids"].shape[1]:]

    # 신규 토큰을 사람이 읽을 수 있는 문자열로 디코딩합니다.
    answer = tokenizer.batch_decode(
        new_tokens,
        skip_special_tokens=True,
    )[0]

    # 앞뒤 공백을 제거하여 최종 답변을 반환합니다.
    return answer.strip()


def main() -> None:
    """
    환경 확인부터 데이터 로드, QLoRA SFT, 평가, 저장, 추론까지 전체 과정을 실행합니다.
    """

    # Python, NumPy, PyTorch 관련 난수 흐름을 가능한 범위에서 고정합니다.
    set_seed(SEED)

    # CUDA GPU가 있을 때 TF32 연산을 허용해 지원 GPU의 연산 성능을 높입니다.
    if torch.cuda.is_available():
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True

    # 실행 환경과 GPU 정보를 출력합니다.
    print_environment()

    # 필요한 데이터 파일이 준비되어 있는지 검사합니다.
    validate_files()

    # 학습 및 검증 데이터셋을 불러옵니다.
    train_dataset, valid_dataset = load_sft_datasets()

    # 기본 모델의 Tokenizer를 불러옵니다.
    tokenizer = load_tokenizer()

    # GPU 지원 상태에 따라 BF16 또는 FP16을 선택합니다.
    compute_dtype = select_compute_dtype()

    # 기본 모델을 4bit 양자화 상태로 불러옵니다.
    model = load_quantized_model(tokenizer, compute_dtype)

    # LoRA Adapter 설정을 생성합니다.
    lora_config = create_lora_config()

    # SFT 학습 설정을 생성합니다.
    training_config = create_training_config(compute_dtype)

    # 모델, 데이터, Tokenizer, LoRA 설정을 연결한 SFTTrainer를 생성합니다.
    trainer = SFTTrainer(
        model=model,
        args=training_config,
        train_dataset=train_dataset,
        eval_dataset=valid_dataset,
        processing_class=tokenizer,
        peft_config=lora_config,
    )

    # LoRA가 적용된 이후의 전체/학습 가능 파라미터를 계산합니다.
    parameter_info = count_parameters(trainer.model)

    # 계산된 파라미터 정보를 출력합니다.
    print("\n" + "=" * 80)
    print("6. 학습 파라미터 확인")
    print("=" * 80)
    print(f"전체 파라미터     : {parameter_info['total_parameters']:,}")
    print(f"학습 파라미터     : {parameter_info['trainable_parameters']:,}")
    print(f"학습 파라미터 비율: {parameter_info['trainable_ratio']:.4f}%")

    # PEFT 모델이 제공하는 학습 가능 파라미터 출력 기능을 실행합니다.
    if hasattr(trainer.model, "print_trainable_parameters"):
        trainer.model.print_trainable_parameters()

    # 실제 SFT 학습을 시작합니다.
    print("\n" + "=" * 80)
    print("7. Supervised Fine-Tuning 시작")
    print("=" * 80)
    train_result = trainer.train()

    # 학습 완료 후 최종 Training Loss를 출력합니다.
    print("\n" + "=" * 80)
    print("8. 학습 완료")
    print("=" * 80)
    print(f"최종 Training Loss : {train_result.training_loss}")

    # Trainer가 반환한 학습 지표를 가져옵니다.
    train_metrics = train_result.metrics

    # 실제 학습 샘플 수를 지표에 추가합니다.
    train_metrics["train_samples"] = len(train_dataset)

    # 학습 지표를 콘솔에 출력합니다.
    trainer.log_metrics("train", train_metrics)

    # 학습 지표를 JSON 파일로 저장합니다.
    trainer.save_metrics("train", train_metrics)

    # Optimizer, Scheduler, Global Step 등 Trainer 상태를 저장합니다.
    trainer.save_state()

    # 검증 데이터로 최종 평가를 수행합니다.
    eval_metrics = trainer.evaluate()

    # 검증 샘플 수를 평가 지표에 추가합니다.
    eval_metrics["eval_samples"] = len(valid_dataset)

    # 평가 지표를 콘솔에 출력합니다.
    trainer.log_metrics("eval", eval_metrics)

    # 평가 지표를 JSON 파일로 저장합니다.
    trainer.save_metrics("eval", eval_metrics)

    # 가장 좋은 LoRA Adapter를 최종 출력 폴더에 저장합니다.
    trainer.save_model(str(OUTPUT_DIR))

    # 추론 시 같은 Chat Template과 Tokenizer를 사용하도록 함께 저장합니다.
    tokenizer.save_pretrained(str(OUTPUT_DIR))

    # 주요 학습 설정과 결과를 별도 요약 JSON 파일로 저장합니다.
    save_json(
        {
            "base_model": MODEL_NAME,
            "output_dir": str(OUTPUT_DIR),
            "max_length": MAX_LENGTH,
            "train_batch_size": TRAIN_BATCH_SIZE,
            "eval_batch_size": EVAL_BATCH_SIZE,
            "gradient_accumulation_steps": GRADIENT_ACCUMULATION_STEPS,
            "effective_batch_size": (
                TRAIN_BATCH_SIZE * GRADIENT_ACCUMULATION_STEPS
            ),
            "num_train_epochs": NUM_TRAIN_EPOCHS,
            "learning_rate": LEARNING_RATE,
            "weight_decay": WEIGHT_DECAY,
            "warmup_ratio": WARMUP_RATIO,
            "compute_dtype": str(compute_dtype),
            "lora_r": lora_config.r,
            "lora_alpha": lora_config.lora_alpha,
            "lora_dropout": lora_config.lora_dropout,
            "target_modules": list(lora_config.target_modules),
            "parameter_info": parameter_info,
            "train_metrics": train_metrics,
            "eval_metrics": eval_metrics,
        },
        OUTPUT_DIR / "training_summary.json",
    )

    # 학습된 모델의 기본 동작을 확인할 테스트 질문을 지정합니다.
    test_question = "배송 완료로 나오지만 상품을 받지 못했습니다."

    # 테스트 질문을 출력합니다.
    print("\n" + "=" * 80)
    print("9. 학습 모델 추론 테스트")
    print("=" * 80)
    print(f"[질문]\n{test_question}")

    # 현재 학습된 모델로 답변을 생성합니다.
    test_answer = run_test_inference(
        model=trainer.model,
        tokenizer=tokenizer,
        question=test_question,
    )

    # 생성된 답변을 출력합니다.
    print(f"\n[답변]\n{test_answer}")

    # 테스트 질문과 답변을 JSON 파일로 저장합니다.
    save_json(
        {
            "question": test_question,
            "answer": test_answer,
        },
        OUTPUT_DIR / "test_generation.json",
    )

    # 최종 저장 위치와 다음 실행 명령을 안내합니다.
    print("\n" + "=" * 80)
    print("10. 전체 파이프라인 완료")
    print("=" * 80)
    print(f"LoRA Adapter 저장 위치 : {OUTPUT_DIR}")
    print("저장된 Adapter 추론 명령: python 03_inference.py")

    # Trainer와 원본 모델 참조를 제거합니다.
    del trainer
    del model

    # 파이썬 가비지 컬렉션을 실행합니다.
    gc.collect()

    # 사용하지 않는 CUDA 캐시 메모리를 해제합니다.
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


# 파일을 직접 실행했을 때만 전체 학습 파이프라인을 시작합니다.
if __name__ == "__main__":
    main()
