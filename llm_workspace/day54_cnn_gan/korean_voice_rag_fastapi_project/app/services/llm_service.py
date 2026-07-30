"""전체 파인튜닝 모델과 PEFT LoRA 어댑터를 안전하게 지원합니다."""
from pathlib import Path  # 모델 경로와 모델 구성 파일을 검사합니다.
from threading import Lock  # 여러 요청이 동시에 모델을 중복 로딩하지 않도록 보호합니다.
import logging  # 모델 로딩 실패 원인을 서버 터미널에 기록합니다.
from app.config import settings  # LLM 관련 환경 설정을 가져옵니다.

logger = logging.getLogger(__name__)  # 현재 모듈 전용 로거를 생성합니다.


class FineTunedLlmService:
    """검색 근거를 이용해 한국어 답변을 생성하는 서비스입니다."""

    def __init__(self) -> None:
        self._tokenizer = None  # Hugging Face 토크나이저 객체를 저장합니다.
        self._model = None  # Hugging Face 또는 PEFT 모델 객체를 저장합니다.
        self._mode = "not_loaded"  # 현재 모델 실행 상태를 기록합니다.
        self._load_error = None  # 마지막 모델 로딩 오류 내용을 기록합니다.
        self._lock = Lock()  # 최초 모델 로딩 구간을 스레드 안전하게 보호합니다.

    @property
    def mode(self) -> str:
        return self._mode  # 상태 확인 API와 응답 화면에 현재 모드를 제공합니다.

    @property
    def load_error(self) -> str | None:
        return self._load_error  # 상태 확인 API에서 마지막 로딩 오류를 확인하도록 제공합니다.

    def _device(self) -> str:
        """환경 설정과 CUDA 사용 가능 여부를 기준으로 실행 장치를 선택합니다."""
        if settings.LLM_DEVICE in {"cpu", "cuda"}:
            return settings.LLM_DEVICE  # 사용자가 cpu 또는 cuda를 명시했다면 그대로 사용합니다.
        import torch  # 자동 장치 선택을 위해 PyTorch를 지연 임포트합니다.
        return "cuda" if torch.cuda.is_available() else "cpu"  # GPU가 있으면 CUDA, 없으면 CPU를 사용합니다.

    @staticmethod
    def _has_full_model_files(path: Path) -> bool:
        """폴더 안에 실제 전체 모델 파일이 있는지 검사합니다."""
        config_exists = (path / "config.json").is_file()  # 전체 모델 설정 파일 존재 여부를 확인합니다.
        weight_patterns = ("*.safetensors", "pytorch_model*.bin", "model*.bin")  # 대표적인 가중치 파일 패턴을 정의합니다.
        weight_exists = any(any(path.glob(pattern)) for pattern in weight_patterns)  # 패턴 중 하나라도 실제 파일이 있는지 확인합니다.
        return config_exists and weight_exists  # 설정 파일과 가중치 파일이 모두 있어야 전체 모델로 인정합니다.

    @staticmethod
    def _has_adapter_files(path: Path) -> bool:
        """폴더 안에 실제 PEFT LoRA 어댑터 파일이 있는지 검사합니다."""
        config_exists = (path / "adapter_config.json").is_file()  # PEFT 어댑터 설정 파일을 확인합니다.
        weight_exists = (path / "adapter_model.safetensors").is_file() or (path / "adapter_model.bin").is_file()  # 어댑터 가중치 파일을 확인합니다.
        return config_exists and weight_exists  # 설정과 가중치가 모두 있을 때만 어댑터로 인정합니다.

    def _use_demo_fallback(self, reason: str) -> None:
        """모델을 사용할 수 없을 때 RAG 검색 결과만으로 동작하는 안전 모드로 전환합니다."""
        self._tokenizer = None  # 부분적으로 로딩된 토크나이저를 제거합니다.
        self._model = None  # 부분적으로 로딩된 모델 객체를 제거합니다.
        self._mode = "demo_fallback"  # 서비스가 중단되지 않도록 데모 모드로 전환합니다.
        self._load_error = reason  # 전환 원인을 상태 정보로 보관합니다.
        logger.warning("LLM 데모 대체 모드로 전환: %s", reason)  # PyCharm 터미널에 원인을 기록합니다.

    def _load(self) -> None:
        """전체 모델 또는 LoRA 어댑터를 최초 요청 시 한 번만 로딩합니다."""
        if self._model is not None or self._mode == "demo_fallback":
            return  # 이미 모델이 준비되었거나 대체 모드로 결정되었다면 다시 로딩하지 않습니다.

        with self._lock:
            if self._model is not None or self._mode == "demo_fallback":
                return  # 다른 요청이 먼저 로딩을 마쳤는지 잠금 내부에서 다시 확인합니다.

            path = settings.FINETUNED_MODEL_PATH  # config.py에서 절대 경로로 정규화된 모델 폴더를 가져옵니다.
            is_adapter = self._has_adapter_files(path)  # 유효한 LoRA 어댑터 파일 집합인지 검사합니다.
            is_full_model = self._has_full_model_files(path)  # 유효한 전체 모델 파일 집합인지 검사합니다.

            if not is_adapter and not is_full_model:
                reason = (
                    f"유효한 파인튜닝 모델 파일이 없습니다: {path}. "
                    "README.md만 있는 폴더는 모델로 인식하지 않습니다."
                )  # 사용자가 바로 원인을 이해할 수 있는 안내 문구를 만듭니다.
                if settings.ALLOW_DEMO_FALLBACK:
                    self._use_demo_fallback(reason)  # 모델이 없으면 500 오류 대신 RAG 데모 모드로 전환합니다.
                    return
                raise FileNotFoundError(reason)  # 엄격 모드에서는 모델 누락 오류를 명확히 발생시킵니다.

            try:
                import torch  # 모델 자료형과 추론 모드에 사용할 PyTorch를 가져옵니다.
                from transformers import AutoModelForCausalLM, AutoTokenizer  # Hugging Face 모델 클래스를 가져옵니다.

                device = self._device()  # CPU 또는 CUDA 실행 장치를 선택합니다.
                dtype = torch.float16 if device == "cuda" else torch.float32  # GPU에서는 FP16, CPU에서는 FP32를 사용합니다.
                tokenizer_source = settings.BASE_MODEL_NAME if is_adapter else str(path)  # 어댑터는 베이스 모델 토크나이저를 사용합니다.
                self._tokenizer = AutoTokenizer.from_pretrained(
                    tokenizer_source,
                    trust_remote_code=True,
                    use_fast=True,
                )  # 모델에 맞는 토크나이저를 로딩합니다.

                if self._tokenizer.pad_token_id is None:
                    self._tokenizer.pad_token_id = self._tokenizer.eos_token_id  # 패딩 토큰이 없으면 종료 토큰으로 보정합니다.

                if is_adapter:
                    from peft import PeftModel  # LoRA 어댑터 결합 클래스를 가져옵니다.
                    base = AutoModelForCausalLM.from_pretrained(
                        settings.BASE_MODEL_NAME,
                        torch_dtype=dtype,
                        trust_remote_code=True,
                        low_cpu_mem_usage=True,
                    )  # 학습 당시 사용한 원본 베이스 모델을 로딩합니다.
                    self._model = PeftModel.from_pretrained(base, str(path))  # 베이스 모델에 학습된 어댑터를 결합합니다.
                    self._mode = "peft_adapter"  # 현재 실행 모드를 PEFT 어댑터로 기록합니다.
                else:
                    self._model = AutoModelForCausalLM.from_pretrained(
                        str(path),
                        torch_dtype=dtype,
                        trust_remote_code=True,
                        low_cpu_mem_usage=True,
                    )  # 로컬 폴더의 전체 파인튜닝 모델을 로딩합니다.
                    self._mode = "full_finetuned_model"  # 현재 실행 모드를 전체 모델로 기록합니다.

                self._model.to(device).eval()  # 모델을 실행 장치로 이동하고 평가 모드로 전환합니다.
                self._load_error = None  # 정상 로딩되었으므로 이전 오류 내용을 제거합니다.
            except Exception as exc:
                reason = f"파인튜닝 모델 로딩 실패: {type(exc).__name__}: {exc}"  # 실제 오류 형식과 메시지를 함께 보관합니다.
                if settings.ALLOW_DEMO_FALLBACK:
                    self._use_demo_fallback(reason)  # 라이브러리·메모리·모델 문제 발생 시에도 서비스 전체 중단을 막습니다.
                    return
                raise RuntimeError(reason) from exc  # 엄격 모드에서는 원인을 보존한 채 오류를 전달합니다.

    def _demo_answer(self, question: str, contexts: list[dict]) -> str:
        """LLM이 없을 때 검색 문서 내용을 기반으로 안전한 데모 답변을 만듭니다."""
        if not contexts:
            return (
                "현재 파인튜닝 모델이 준비되지 않았고 검색된 RAG 문서도 없습니다. "
                "models/finetuned_model 폴더에 모델을 배치하고 data/documents 폴더에 문서를 추가해 주세요."
            )  # 모델과 문서가 모두 없을 때 준비 방법을 안내합니다.

        best = contexts[0]  # 유사도가 가장 높은 첫 번째 문서 조각을 선택합니다.
        evidence = best["text"][:900].strip()  # 화면과 음성에 지나치게 긴 내용이 전달되지 않도록 길이를 제한합니다.
        return (
            f"질문하신 내용에 대해 검색 문서에서 확인된 정보는 다음과 같습니다.\n\n"
            f"{evidence}\n\n"
            f"현재는 파인튜닝 모델이 배치되지 않아 검색 근거를 직접 안내하는 데모 모드입니다.\n"
            f"근거: {best['source']}"
        )  # RAG 근거와 현재 실행 모드를 명확히 포함한 답변을 반환합니다.

    def generate(self, question: str, contexts: list[dict]) -> str:
        """검색 근거와 질문을 이용해 최종 한국어 답변을 생성합니다."""
        self._load()  # 첫 질문에서 모델 또는 데모 모드를 준비합니다.

        if self._mode == "demo_fallback":
            return self._demo_answer(question, contexts)  # 모델이 없거나 로딩에 실패하면 RAG 데모 답변을 반환합니다.

        import torch  # 모델 추론 시 그래디언트 비활성화를 위해 PyTorch를 가져옵니다.
        context_text = "\n\n".join(
            f"[근거 {index + 1}: {context['source']}#{context['chunk_id']}]\n{context['text']}"
            for index, context in enumerate(contexts)
        ) or "검색된 근거가 없습니다."  # 검색 문서를 모델이 이해할 수 있는 근거 블록으로 구성합니다.

        messages = [
            {
                "role": "system",
                "content": (
                    "당신은 한국어 RAG 상담원입니다. 제공된 검색 근거를 우선 사용하고, "
                    "근거에 없는 내용은 추측하지 말며, 근거가 부족하면 부족하다고 명확히 말하세요."
                ),
            },
            {
                "role": "user",
                "content": f"{context_text}\n\n질문: {question}\n답변 마지막에 근거 파일명을 표시하세요.",
            },
        ]  # 시스템 지침과 사용자 질문을 채팅 메시지 형식으로 구성합니다.

        if hasattr(self._tokenizer, "apply_chat_template"):
            prompt = self._tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
            )  # 채팅 템플릿을 지원하는 모델은 공식 템플릿을 적용합니다.
        else:
            prompt = f"시스템: {messages[0]['content']}\n사용자: {messages[1]['content']}\n도우미:"  # 템플릿이 없는 모델은 일반 텍스트 프롬프트를 사용합니다.

        inputs = self._tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=4096,
        )  # 프롬프트를 모델 입력 토큰으로 변환합니다.
        device = next(self._model.parameters()).device  # 실제 모델이 올라간 장치를 확인합니다.
        inputs = {key: value.to(device) for key, value in inputs.items()}  # 모든 입력 텐서를 모델 장치로 이동합니다.

        generation_options = {
            "max_new_tokens": settings.MAX_NEW_TOKENS,
            "do_sample": settings.TEMPERATURE > 0,
            "repetition_penalty": 1.08,
            "pad_token_id": self._tokenizer.pad_token_id,
            "eos_token_id": self._tokenizer.eos_token_id,
        }  # 공통 생성 옵션을 구성합니다.
        if settings.TEMPERATURE > 0:
            generation_options["temperature"] = max(settings.TEMPERATURE, 0.01)  # 샘플링일 때만 temperature를 전달합니다.
            generation_options["top_p"] = settings.TOP_P  # 샘플링일 때만 누적 확률 범위를 전달합니다.

        with torch.inference_mode():
            output = self._model.generate(**inputs, **generation_options)  # 그래디언트 없이 답변 토큰을 생성합니다.

        answer_ids = output[0][inputs["input_ids"].shape[1]:]  # 입력 프롬프트에 해당하는 토큰을 결과에서 제외합니다.
        answer = self._tokenizer.decode(answer_ids, skip_special_tokens=True).strip()  # 생성 토큰을 한국어 문자열로 복원합니다.
        return answer or "답변을 생성하지 못했습니다."  # 빈 출력이면 사용자에게 명확한 안내를 반환합니다.
