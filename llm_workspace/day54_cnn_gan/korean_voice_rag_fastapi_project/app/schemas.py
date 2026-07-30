"""FastAPI 요청과 응답 구조를 정의합니다."""
from pydantic import BaseModel, Field  # 입력 검증용 Pydantic 클래스를 가져옵니다.

class TextQuestionRequest(BaseModel):
    """텍스트 질문 요청입니다."""
    question: str = Field(..., min_length=1)  # 한 글자 이상의 질문을 받습니다.
    speak: bool = True  # TTS 생성 여부를 받습니다.

class SourceItem(BaseModel):
    """검색 근거 한 건입니다."""
    source: str  # 원본 파일명입니다.
    chunk_id: int  # 문서 조각 번호입니다.
    score: float  # 코사인 유사도입니다.
    preview: str  # 화면 표시용 일부 내용입니다.

class AskResponse(BaseModel):
    """질문 처리 공통 응답입니다."""
    question: str  # 최종 질문입니다.
    answer: str  # LLM 답변입니다.
    sources: list[SourceItem]  # 검색 근거 목록입니다.
    audio_url: str | None  # TTS 음성 URL입니다.
    model_mode: str  # 실제 모델 또는 데모 모드입니다.
