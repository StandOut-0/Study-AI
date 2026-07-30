"""SentenceTransformer 기반 로컬 RAG 검색 서비스입니다."""
from dataclasses import dataclass  # 문서 조각 데이터 구조를 정의합니다.
from threading import Lock  # 인덱스 중복 생성을 방지합니다.
import numpy as np  # 벡터 내적과 정렬에 사용합니다.
from app.config import settings  # RAG 설정과 문서 경로를 가져옵니다.

@dataclass
class Chunk:
    source: str  # 원본 파일명입니다.
    chunk_id: int  # 파일 내부 조각 번호입니다.
    text: str  # 검색 대상 텍스트입니다.

class RagService:
    """TXT와 MD 문서를 임베딩하여 의미 검색합니다."""
    def __init__(self) -> None:
        self._model = None  # 임베딩 모델을 저장합니다.
        self._chunks: list[Chunk] = []  # 문서 조각을 저장합니다.
        self._embeddings = None  # 정규화 임베딩 행렬을 저장합니다.
        self._lock = Lock()  # 최초 인덱싱을 보호합니다.

    def _split(self, text: str) -> list[str]:
        text = ' '.join(text.split())  # 연속 공백과 줄바꿈을 정리합니다.
        result, start = [], 0  # 결과 목록과 시작 위치를 초기화합니다.
        while start < len(text):  # 문서 끝까지 반복합니다.
            end = min(start + settings.CHUNK_SIZE, len(text))  # 현재 조각 끝 위치를 계산합니다.
            part = text[start:end].strip()  # 현재 범위 문자열을 추출합니다.
            if part: result.append(part)  # 비어 있지 않은 조각을 추가합니다.
            if end >= len(text): break  # 문서 끝이면 반복을 종료합니다.
            start = max(end - settings.CHUNK_OVERLAP, start + 1)  # 겹침을 유지한 다음 시작점을 계산합니다.
        return result  # 완성된 조각 목록을 반환합니다.

    def _build(self) -> None:
        if self._embeddings is not None: return  # 인덱스가 있으면 재사용합니다.
        with self._lock:  # 최초 생성 구간을 잠급니다.
            if self._embeddings is not None: return  # 다른 요청이 생성했는지 재확인합니다.
            from sentence_transformers import SentenceTransformer  # 임베딩 모델을 지연 가져옵니다.
            self._model = SentenceTransformer(settings.EMBEDDING_MODEL_NAME)  # 다국어 모델을 로드합니다.
            self._chunks = []  # 기존 문서 조각을 초기화합니다.
            settings.DOCUMENT_DIR.mkdir(parents=True, exist_ok=True)  # 문서 디렉터리를 보장합니다.
            paths = sorted(list(settings.DOCUMENT_DIR.glob('*.txt')) + list(settings.DOCUMENT_DIR.glob('*.md')))  # 지원 문서를 조회합니다.
            for path in paths:  # 각 파일을 순회합니다.
                text = path.read_text(encoding='utf-8')  # 한글 보존을 위해 UTF-8로 읽습니다.
                for idx, part in enumerate(self._split(text)):  # 문서를 조각으로 나눕니다.
                    self._chunks.append(Chunk(path.name, idx, part))  # 메타데이터와 함께 저장합니다.
            if not self._chunks:  # 문서가 없으면 빈 배열을 저장합니다.
                self._embeddings = np.empty((0, 0), dtype=np.float32)
                return
            passages = [f'passage: {item.text}' for item in self._chunks]  # E5 문서 접두어를 붙입니다.
            self._embeddings = self._model.encode(passages, convert_to_numpy=True, normalize_embeddings=True, show_progress_bar=False).astype(np.float32)  # 문서 임베딩을 생성합니다.

    def search(self, question: str) -> list[dict]:
        self._build()  # 최초 요청에서 인덱스를 준비합니다.
        if not self._chunks or self._embeddings.size == 0: return []  # 검색 대상이 없으면 빈 목록을 반환합니다.
        query = self._model.encode([f'query: {question}'], convert_to_numpy=True, normalize_embeddings=True, show_progress_bar=False)[0].astype(np.float32)  # 질문 임베딩을 생성합니다.
        scores = self._embeddings @ query  # 정규화 벡터 내적으로 코사인 유사도를 계산합니다.
        indices = np.argsort(scores)[::-1][:settings.RAG_TOP_K]  # 점수 상위 조각을 선택합니다.
        return [{'source': self._chunks[int(i)].source, 'chunk_id': self._chunks[int(i)].chunk_id, 'text': self._chunks[int(i)].text, 'score': float(scores[int(i)])} for i in indices]  # API용 딕셔너리 목록을 반환합니다.

    def rebuild(self) -> int:
        with self._lock:  # 인덱스 초기화를 보호합니다.
            self._chunks, self._embeddings = [], None  # 기존 상태를 제거합니다.
        self._build()  # 새 문서 인덱스를 생성합니다.
        return len(self._chunks)  # 문서 조각 수를 반환합니다.
