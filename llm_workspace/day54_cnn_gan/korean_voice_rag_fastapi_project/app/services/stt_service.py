"""Faster-Whisper 한국어 STT 서비스입니다."""
from pathlib import Path  # 음성 파일 경로를 처리합니다.
from threading import Lock  # 모델 중복 로딩을 방지합니다.
from app.config import settings  # STT 설정을 가져옵니다.

class SpeechToTextService:
    """음성 파일을 한국어 문자열로 변환합니다."""
    def __init__(self) -> None:
        self._model = None  # 실제 WhisperModel을 지연 저장합니다.
        self._lock = Lock()  # 최초 로딩 동시 실행을 막습니다.

    def _device(self) -> str:
        if settings.WHISPER_DEVICE in {'cpu', 'cuda'}:  # 장치가 명시되었는지 확인합니다.
            return settings.WHISPER_DEVICE  # 명시한 장치를 반환합니다.
        try:
            import torch  # CUDA 사용 가능 여부 확인용입니다.
            return 'cuda' if torch.cuda.is_available() else 'cpu'  # 자동 장치 선택 결과를 반환합니다.
        except ImportError:
            return 'cpu'  # torch가 없으면 CPU를 선택합니다.

    def _get_model(self):
        if self._model is not None:  # 이미 로딩했으면 재사용합니다.
            return self._model
        with self._lock:  # 모델 최초 로딩 구간을 잠급니다.
            if self._model is None:
                from faster_whisper import WhisperModel  # 필요 시점에 패키지를 가져옵니다.
                device = self._device()  # 실행 장치를 계산합니다.
                compute_type = 'float16' if device == 'cuda' and settings.WHISPER_COMPUTE_TYPE == 'int8' else settings.WHISPER_COMPUTE_TYPE  # GPU 정밀도를 보정합니다.
                self._model = WhisperModel(settings.WHISPER_MODEL_SIZE, device=device, compute_type=compute_type)  # STT 모델을 생성합니다.
        return self._model  # 준비된 모델을 반환합니다.

    def transcribe(self, audio_path: Path) -> str:
        if not audio_path.exists():  # 파일 존재 여부를 검사합니다.
            raise FileNotFoundError(str(audio_path))  # 파일이 없으면 오류를 발생시킵니다.
        segments, _ = self._get_model().transcribe(str(audio_path), language='ko', task='transcribe', vad_filter=True, beam_size=5, condition_on_previous_text=False)  # 한국어 음성 인식을 실행합니다.
        text = ' '.join(segment.text.strip() for segment in segments if segment.text.strip()).strip()  # 구간별 텍스트를 하나로 연결합니다.
        if not text:  # 인식 결과가 비었는지 검사합니다.
            raise ValueError('음성을 인식하지 못했습니다. 다시 말해 주세요.')  # 사용자 친화적 오류를 발생시킵니다.
        return text  # UTF-8 파이썬 문자열을 반환합니다.
