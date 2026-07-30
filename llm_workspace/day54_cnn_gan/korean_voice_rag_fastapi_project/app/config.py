"""환경 변수와 프로젝트 경로를 안전하게 관리합니다."""
import os  # 운영체제 환경 변수를 읽습니다.
from pathlib import Path  # 운영체제 독립적인 경로 처리를 지원합니다.
from dotenv import load_dotenv  # 프로젝트의 .env 파일을 현재 프로세스에 로딩합니다.

BASE_DIR = Path(__file__).resolve().parent.parent  # app 폴더의 상위인 프로젝트 최상위 경로를 계산합니다.
load_dotenv(BASE_DIR / ".env")  # 실행 위치와 관계없이 프로젝트 루트의 .env 파일을 읽습니다.


def _project_path(value: str, default: Path) -> Path:
    """환경 변수의 상대 경로를 프로젝트 루트 기준 절대 경로로 변환합니다."""
    raw_path = Path(value).expanduser() if value else default  # 환경 값이 있으면 사용하고 없으면 기본 경로를 선택합니다.
    return raw_path.resolve() if raw_path.is_absolute() else (BASE_DIR / raw_path).resolve()  # 상대 경로는 프로젝트 루트에 결합합니다.


class Settings:
    """애플리케이션 전체에서 공유하는 설정 모음입니다."""
    APP_NAME = os.getenv("APP_NAME", "한국어 음성 RAG 서비스")  # 브라우저와 API 문서에 표시할 서비스 이름입니다.
    HOST = os.getenv("HOST", "127.0.0.1")  # FastAPI 서버가 바인딩할 주소입니다.
    PORT = int(os.getenv("PORT", "8000"))  # FastAPI 서버가 사용할 포트 번호입니다.
    FINETUNED_MODEL_PATH = _project_path(
        os.getenv("FINETUNED_MODEL_PATH", "models/finetuned_model"),
        BASE_DIR / "models/finetuned_model",
    )  # PyCharm 실행 디렉터리가 달라도 항상 올바른 모델 폴더를 가리키도록 절대 경로로 변환합니다.
    BASE_MODEL_NAME = os.getenv("BASE_MODEL_NAME", "Qwen/Qwen2.5-1.5B-Instruct")  # LoRA 학습 시 사용한 원본 모델 이름입니다.
    ALLOW_DEMO_FALLBACK = os.getenv("ALLOW_DEMO_FALLBACK", "true").lower() == "true"  # 모델이 없거나 실패할 때 RAG 데모 응답을 허용합니다.
    LLM_DEVICE = os.getenv("LLM_DEVICE", "auto").lower()  # LLM 실행 장치로 auto, cpu, cuda 중 하나를 사용합니다.
    MAX_NEW_TOKENS = int(os.getenv("MAX_NEW_TOKENS", "384"))  # 모델이 새로 생성할 최대 토큰 수입니다.
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))  # 답변 생성의 무작위성 정도입니다.
    TOP_P = float(os.getenv("TOP_P", "0.9"))  # 누적 확률 기반 샘플링 범위입니다.
    EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "intfloat/multilingual-e5-small")  # 한국어 문서 검색용 임베딩 모델입니다.
    RAG_TOP_K = int(os.getenv("RAG_TOP_K", "4"))  # 질문마다 가져올 상위 문서 조각 수입니다.
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "700"))  # 각 문서 조각의 최대 문자 수입니다.
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "100"))  # 인접 문서 조각 사이에서 겹칠 문자 수입니다.
    WHISPER_MODEL_SIZE = os.getenv("WHISPER_MODEL_SIZE", "small")  # Faster-Whisper 모델 크기입니다.
    WHISPER_DEVICE = os.getenv("WHISPER_DEVICE", "auto").lower()  # STT 실행 장치입니다.
    WHISPER_COMPUTE_TYPE = os.getenv("WHISPER_COMPUTE_TYPE", "int8")  # STT 계산 정밀도입니다.
    TTS_PROVIDER = os.getenv("TTS_PROVIDER", "edge")  # edge 또는 pyttsx3 중 우선 사용할 TTS 공급자입니다.
    EDGE_TTS_VOICE = os.getenv("EDGE_TTS_VOICE", "ko-KR-SunHiNeural")  # Edge TTS 한국어 음성 이름입니다.
    EDGE_TTS_RATE = os.getenv("EDGE_TTS_RATE", "+0%")  # Edge TTS 발화 속도입니다.
    DOCUMENT_DIR = BASE_DIR / "data/documents"  # RAG가 읽을 UTF-8 TXT와 MD 문서 폴더입니다.
    UPLOAD_DIR = BASE_DIR / "storage/uploads"  # 브라우저에서 전달된 녹음 파일 저장 폴더입니다.
    AUDIO_DIR = BASE_DIR / "storage/audio"  # TTS가 생성한 음성 파일 저장 폴더입니다.
    STATIC_DIR = BASE_DIR / "app/static"  # HTML, CSS, JavaScript 정적 파일 폴더입니다.


settings = Settings()  # 다른 모듈에서 재사용할 단일 설정 객체를 생성합니다.
