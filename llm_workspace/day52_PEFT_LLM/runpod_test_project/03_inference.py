"""
저장된 Qwen2.5 기본 모델과 LoRA Adapter를 결합하여
한국어 고객 상담 답변을 생성하는 대화형 추론 코드입니다.
"""

# 환경변수를 읽기 위해 os 모듈을 사용합니다.
import os

# 파일 및 디렉터리 경로를 안전하게 처리합니다.
from pathlib import Path

# 모델의 GPU 연산과 추론을 수행합니다.
import torch

# .env 파일을 현재 실행 환경에 로드합니다.
from dotenv import load_dotenv

# 저장된 LoRA Adapter를 기본 모델에 연결합니다.
from peft import PeftModel

# 기본 모델, Tokenizer 및 4bit 양자화 설정을 불러옵니다.
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
)


# 현재 파일의 폴더를 프로젝트 루트로 지정합니다.
BASE_DIR = Path(__file__).resolve().parent

# 프로젝트 루트에 있는 .env 파일을 불러옵니다.
load_dotenv(BASE_DIR / ".env")

# 학습 때 사용한 기본 모델 이름을 환경변수에서 읽습니다.
BASE_MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "Qwen/Qwen2.5-0.5B-Instruct",
)

# 학습된 LoRA Adapter의 저장 경로를 지정합니다.
ADAPTER_DIR = BASE_DIR / os.getenv(
    "OUTPUT_DIR",
    "outputs/qwen2.5-korean-sft-lora",
)

# 비공개 또는 승인형 모델에 사용할 Hugging Face 토큰을 읽습니다.
HF_TOKEN = os.getenv("HF_TOKEN") or None


def select_compute_dtype() -> torch.dtype:
    """
    GPU의 BF16 지원 여부에 따라 추론 연산 타입을 선택합니다.
    """

    # CUDA GPU가 존재하고 BF16을 지원하면 BF16을 반환합니다.
    if torch.cuda.is_available() and torch.cuda.is_bf16_supported():
        return torch.bfloat16

    # BF16을 사용할 수 없으면 FP16을 반환합니다.
    return torch.float16


def load_model_and_tokenizer():
    """
    기본 모델, Tokenizer 및 학습된 LoRA Adapter를 불러옵니다.
    """

    # Adapter 디렉터리가 없으면 학습 코드를 먼저 실행하도록 오류를 발생시킵니다.
    if not ADAPTER_DIR.exists():
        raise FileNotFoundError(
            f"LoRA Adapter를 찾을 수 없습니다: {ADAPTER_DIR}\n"
            "먼저 python 02_train_sft.py를 실행하세요."
        )

    # GPU 지원 상태에 따라 BF16 또는 FP16을 선택합니다.
    compute_dtype = select_compute_dtype()

    # 추론용 4bit NF4 양자화 설정을 생성합니다.
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=compute_dtype,
    )

    # 학습 시 저장한 Tokenizer를 Adapter 폴더에서 불러옵니다.
    tokenizer = AutoTokenizer.from_pretrained(
        str(ADAPTER_DIR),
        trust_remote_code=True,
    )

    # Padding Token이 없을 때 EOS Token을 대신 사용합니다.
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # 기본 사전 학습 모델을 4bit 상태로 첫 번째 GPU에 불러옵니다.
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_NAME,
        quantization_config=quantization_config,
        device_map={"": 0},
        trust_remote_code=True,
        token=HF_TOKEN,
    )

    # 모델과 Tokenizer의 Padding Token ID를 동일하게 맞춥니다.
    base_model.config.pad_token_id = tokenizer.pad_token_id

    # 기본 모델 위에 학습된 LoRA Adapter를 연결합니다.
    model = PeftModel.from_pretrained(
        base_model,
        str(ADAPTER_DIR),
    )

    # 반복 추론 속도를 높이기 위해 KV Cache를 활성화합니다.
    model.config.use_cache = True

    # Dropout 등을 비활성화하도록 평가 모드로 전환합니다.
    model.eval()

    # Adapter가 결합된 모델과 Tokenizer를 반환합니다.
    return model, tokenizer


def generate_answer(model, tokenizer, question: str) -> str:
    """
    사용자 질문에 대한 모델 답변을 생성합니다.
    """

    # 모델에 전달할 system/user 메시지를 구성합니다.
    messages = [
        {
            "role": "system",
            "content": (
                "당신은 온라인 쇼핑몰의 고객 상담 AI입니다. "
                "고객의 질문을 정확히 이해하고 친절하게 답변하세요. "
                "확인되지 않은 사실은 임의로 만들지 마세요."
            ),
        },
        {
            "role": "user",
            "content": question,
        },
    ]

    # Qwen 모델 전용 Chat Template을 적용해 문자열 프롬프트를 만듭니다.
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    # 문자열 프롬프트를 input_ids와 attention_mask Tensor로 변환합니다.
    inputs = tokenizer(prompt, return_tensors="pt")

    # 입력 Tensor를 모델이 위치한 GPU로 이동합니다.
    inputs = {
        key: value.to(model.device)
        for key, value in inputs.items()
    }

    # Gradient를 계산하지 않는 추론 전용 모드로 답변을 생성합니다.
    with torch.inference_mode():
        generated_ids = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
            repetition_penalty=1.1,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )

    # 입력 프롬프트를 제외하고 새로 생성된 답변 토큰만 가져옵니다.
    generated_tokens = generated_ids[:, inputs["input_ids"].shape[1]:]

    # 생성 토큰을 사람이 읽을 수 있는 문자열로 변환합니다.
    answer = tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True,
    )[0]

    # 앞뒤 공백을 제거한 답변을 반환합니다.
    return answer.strip()


def main() -> None:
    """
    모델을 한 번 불러온 뒤 사용자의 질문을 반복 처리합니다.
    """

    # 프로그램 제목을 출력합니다.
    print("=" * 70)
    print("Qwen2.5 한국어 고객 상담 SFT 모델")
    print("=" * 70)

    # 기본 모델, LoRA Adapter 및 Tokenizer를 불러옵니다.
    model, tokenizer = load_model_and_tokenizer()

    # 모델 로드 완료와 종료 명령을 안내합니다.
    print("모델과 LoRA Adapter 로드가 완료되었습니다.")
    print("'종료', 'exit' 또는 'quit'을 입력하면 종료됩니다.")

    # 사용자가 종료 명령을 입력할 때까지 질문을 반복해서 받습니다.
    while True:
        # 터미널에서 사용자 질문을 입력받고 앞뒤 공백을 제거합니다.
        question = input("\n질문: ").strip()

        # 종료 명령이 입력되면 반복문을 종료합니다.
        if question.lower() in {"종료", "exit", "quit"}:
            print("프로그램을 종료합니다.")
            break

        # 빈 문자열이 입력되면 안내 후 다시 질문을 받습니다.
        if not question:
            print("질문을 입력해 주세요.")
            continue

        # 모델을 호출하여 질문에 대한 답변을 생성합니다.
        answer = generate_answer(
            model=model,
            tokenizer=tokenizer,
            question=question,
        )

        # 생성된 답변을 화면에 출력합니다.
        print(f"\n답변: {answer}")


# 이 파일을 직접 실행했을 때만 대화형 추론 프로그램을 시작합니다.
if __name__ == "__main__":
    main()

# 토크나이저 관련 에러가 발생하면 해당 패키지를 직접 다시 설치합니다.
# runpod ssh 터미널에서
# python -m pip install --upgrade sentencepiece tiktoken tokenizers transformers