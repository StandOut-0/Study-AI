"""한국어 리뷰 문장을 단순 토큰화하고 정수 ID로 변환하는 유틸리티입니다."""

# json은 단어 사전을 파일로 저장하고 다시 불러오기 위해 사용합니다.
import json

# re는 한글, 영어, 숫자, 공백 외의 문자를 정리하기 위해 사용합니다.
import re

# Counter는 학습 데이터에서 단어 빈도를 계산하기 위해 사용합니다.
from collections import Counter

# Path는 저장 경로를 안전하게 다루기 위해 사용합니다.
from pathlib import Path


# Vocabulary 클래스는 단어와 정수 ID 사이의 매핑을 관리합니다.
class Vocabulary:
    # __init__ 메서드는 특수 토큰과 단어 사전 자료구조를 초기화합니다.
    def __init__(self, max_size: int = 30000, min_freq: int = 2):
        # 사용할 최대 단어 수를 저장합니다.
        self.max_size = max_size
        # 단어 사전에 포함할 최소 등장 빈도를 저장합니다.
        self.min_freq = min_freq
        # padding 토큰은 짧은 문장을 같은 길이로 맞출 때 사용합니다.
        self.pad_token = "<PAD>"
        # unknown 토큰은 사전에 없는 단어를 표현할 때 사용합니다.
        self.unk_token = "<UNK>"
        # 단어를 정수 ID로 바꾸는 딕셔너리를 초기화합니다.
        self.stoi = {self.pad_token: 0, self.unk_token: 1}
        # 정수 ID를 단어로 바꾸는 딕셔너리를 초기화합니다.
        self.itos = {0: self.pad_token, 1: self.unk_token}

    # __len__ 메서드는 현재 단어 사전 크기를 반환합니다.
    def __len__(self) -> int:
        # stoi 딕셔너리의 길이가 전체 토큰 개수입니다.
        return len(self.stoi)

    # tokenize 메서드는 한국어 문장을 공백 기준 토큰 리스트로 변환합니다.
    @staticmethod
    def tokenize(text: str) -> list[str]:
        # 입력값이 문자열이 아니면 빈 문자열로 바꾸어 오류를 방지합니다.
        text = "" if text is None else str(text)
        # 한글, 영어, 숫자, 공백을 제외한 기호를 공백으로 치환합니다.
        text = re.sub(r"[^가-힣a-zA-Z0-9\s]", " ", text)
        # 연속된 공백을 하나의 공백으로 줄이고 앞뒤 공백을 제거합니다.
        text = re.sub(r"\s+", " ", text).strip()
        # 정리된 문장을 공백 기준으로 나누어 토큰 리스트를 만듭니다.
        return text.split()

    # build 메서드는 학습 문장 목록으로 단어 사전을 생성합니다.
    def build(self, texts: list[str]) -> None:
        # 모든 문장의 토큰 빈도를 저장할 Counter 객체를 생성합니다.
        counter = Counter()
        # 학습 문장들을 하나씩 반복합니다.
        for text in texts:
            # 현재 문장을 토큰화한 뒤 빈도 Counter에 더합니다.
            counter.update(self.tokenize(text))
        # 빈도가 높은 단어부터 정렬된 목록을 만듭니다.
        most_common = counter.most_common(self.max_size - 2)
        # 정렬된 단어 목록을 하나씩 확인합니다.
        for word, freq in most_common:
            # 최소 빈도보다 적게 등장한 단어는 사전에 넣지 않습니다.
            if freq < self.min_freq:
                continue
            # 이미 등록된 단어가 아니면 새 ID를 부여합니다.
            if word not in self.stoi:
                # 현재 사전 크기를 새 단어의 ID로 사용합니다.
                idx = len(self.stoi)
                # 단어에서 ID로 가는 매핑을 저장합니다.
                self.stoi[word] = idx
                # ID에서 단어로 가는 매핑을 저장합니다.
                self.itos[idx] = word

    # encode 메서드는 문장을 고정 길이 정수 ID 리스트로 변환합니다.
    def encode(self, text: str, max_len: int) -> list[int]:
        # 문장을 토큰화합니다.
        tokens = self.tokenize(text)
        # 각 토큰을 정수 ID로 바꾸고 사전에 없으면 <UNK> ID를 사용합니다.
        ids = [self.stoi.get(token, self.stoi[self.unk_token]) for token in tokens]
        # 최대 길이를 넘는 문장은 앞에서부터 max_len개만 남깁니다.
        ids = ids[:max_len]
        # 부족한 길이만큼 <PAD> ID를 뒤쪽에 추가합니다.
        ids += [self.stoi[self.pad_token]] * (max_len - len(ids))
        # 완성된 고정 길이 정수 리스트를 반환합니다.
        return ids

    # save 메서드는 단어 사전을 JSON 파일로 저장합니다.
    def save(self, path: str | Path) -> None:
        # 문자열 경로와 Path 경로를 모두 Path 객체로 변환합니다.
        path = Path(path)
        # 부모 폴더가 없으면 자동으로 생성합니다.
        path.parent.mkdir(parents=True, exist_ok=True)
        # 저장할 데이터를 딕셔너리로 구성합니다.
        data = {"max_size": self.max_size, "min_freq": self.min_freq, "stoi": self.stoi}
        # JSON 파일을 UTF-8 인코딩으로 저장합니다.
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    # load 클래스 메서드는 저장된 JSON 파일에서 단어 사전을 복원합니다.
    @classmethod
    def load(cls, path: str | Path) -> "Vocabulary":
        # JSON 파일을 UTF-8 인코딩으로 읽어 딕셔너리로 변환합니다.
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        # 저장된 설정값으로 Vocabulary 객체를 생성합니다.
        vocab = cls(max_size=data["max_size"], min_freq=data["min_freq"])
        # 저장된 stoi 딕셔너리를 복원합니다.
        vocab.stoi = {str(k): int(v) for k, v in data["stoi"].items()}
        # stoi를 뒤집어 itos 딕셔너리를 다시 만듭니다.
        vocab.itos = {idx: word for word, idx in vocab.stoi.items()}
        # 복원된 Vocabulary 객체를 반환합니다.
        return vocab
