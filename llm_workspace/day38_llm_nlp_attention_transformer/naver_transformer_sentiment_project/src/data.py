"""NSMC 데이터를 다운로드하고 PyTorch Dataset/DataLoader로 변환하는 파일입니다."""

# urllib.request는 외부 URL에서 NSMC 텍스트 파일을 다운로드하기 위해 사용합니다.
import urllib.request

# pandas는 탭으로 구분된 NSMC 파일을 DataFrame으로 읽기 위해 사용합니다.
import pandas as pd

# torch는 텐서 변환에 사용합니다.
import torch

# Dataset과 DataLoader는 PyTorch 학습용 데이터 공급 객체를 만들기 위해 사용합니다.
from torch.utils.data import Dataset, DataLoader, random_split

# 프로젝트 설정값을 가져옵니다.
from src.config import TRAIN_URL, TEST_URL, TRAIN_FILE, TEST_FILE, RAW_DATA_DIR, VALID_RATIO, SEED

# Vocabulary 클래스는 한국어 문장을 토큰 ID로 변환하기 위해 사용합니다.
from src.tokenizer import Vocabulary


# download_file 함수는 URL에서 파일을 내려받되, 이미 있으면 다시 받지 않습니다.
def download_file(url: str, path) -> None:
    # 저장 폴더가 없으면 자동으로 생성합니다.
    path.parent.mkdir(parents=True, exist_ok=True)
    # 파일이 이미 존재하고 크기가 0보다 크면 다운로드를 생략합니다.
    if path.exists() and path.stat().st_size > 0:
        # 이미 있는 파일을 그대로 사용하므로 함수를 종료합니다.
        return
    # URL에서 지정 경로로 파일을 다운로드합니다.
    urllib.request.urlretrieve(url, path)


# ensure_nsmc_downloaded 함수는 NSMC 학습/테스트 파일을 준비합니다.
def ensure_nsmc_downloaded() -> None:
    # 원본 데이터 저장 폴더를 생성합니다.
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    # NSMC 학습 데이터 파일을 다운로드합니다.
    download_file(TRAIN_URL, TRAIN_FILE)
    # NSMC 테스트 데이터 파일을 다운로드합니다.
    download_file(TEST_URL, TEST_FILE)


# load_nsmc 함수는 NSMC 파일을 읽고 결측 리뷰를 제거합니다.
def load_nsmc(path) -> pd.DataFrame:
    # NSMC는 id, document, label 컬럼을 가진 탭 구분 텍스트 파일입니다.
    df = pd.read_csv(path, sep="\t")
    # 리뷰 문장 또는 레이블이 없는 행을 제거합니다.
    df = df.dropna(subset=["document", "label"])
    # 레이블을 정수형으로 변환하여 손실 함수 입력 형식에 맞춥니다.
    df["label"] = df["label"].astype(int)
    # 인덱스를 0부터 다시 정리한 DataFrame을 반환합니다.
    return df.reset_index(drop=True)


# NaverReviewDataset 클래스는 리뷰 문장과 감성 레이블을 텐서로 반환합니다.
class NaverReviewDataset(Dataset):
    # __init__ 메서드는 DataFrame, 단어 사전, 최대 길이를 저장합니다.
    def __init__(self, dataframe: pd.DataFrame, vocab: Vocabulary, max_len: int):
        # 리뷰 문장 목록을 문자열 리스트로 저장합니다.
        self.texts = dataframe["document"].astype(str).tolist()
        # 정답 레이블 목록을 정수 리스트로 저장합니다.
        self.labels = dataframe["label"].astype(int).tolist()
        # 문장을 토큰 ID로 바꾸는 단어 사전을 저장합니다.
        self.vocab = vocab
        # 모델 입력 길이를 저장합니다.
        self.max_len = max_len

    # __len__ 메서드는 전체 샘플 개수를 반환합니다.
    def __len__(self) -> int:
        # 리뷰 문장 리스트의 길이가 전체 데이터 개수입니다.
        return len(self.texts)

    # __getitem__ 메서드는 특정 인덱스의 입력 텐서와 레이블 텐서를 반환합니다.
    def __getitem__(self, index: int):
        # 인덱스에 해당하는 리뷰 문장을 가져옵니다.
        text = self.texts[index]
        # 리뷰 문장을 고정 길이 정수 ID 리스트로 변환합니다.
        input_ids = self.vocab.encode(text, self.max_len)
        # 정수 ID 리스트를 LongTensor로 변환합니다.
        x = torch.tensor(input_ids, dtype=torch.long)
        # 정답 레이블을 LongTensor로 변환합니다.
        y = torch.tensor(self.labels[index], dtype=torch.long)
        # 모델 입력과 정답을 튜플로 반환합니다.
        return x, y


# create_dataloaders 함수는 학습/검증/테스트 DataLoader를 생성합니다.
def create_dataloaders(vocab: Vocabulary, max_len: int, batch_size: int, sample_size: int = 0):
    # NSMC 파일이 없으면 다운로드합니다.
    ensure_nsmc_downloaded()
    # 학습 파일을 DataFrame으로 읽습니다.
    train_df = load_nsmc(TRAIN_FILE)
    # 빠른 실습을 위해 sample_size가 양수이면 학습 데이터 일부만 사용합니다.
    if sample_size and sample_size > 0:
        # 지정한 샘플 수만큼 학습 데이터를 앞에서부터 선택합니다.
        train_df = train_df.iloc[:sample_size].copy()
    # 테스트 파일을 DataFrame으로 읽습니다.
    test_df = load_nsmc(TEST_FILE)
    # 전체 학습 데이터셋 객체를 생성합니다.
    full_train_dataset = NaverReviewDataset(train_df, vocab, max_len)
    # 테스트 데이터셋 객체를 생성합니다.
    test_dataset = NaverReviewDataset(test_df, vocab, max_len)
    # 검증 데이터 개수를 계산합니다.
    valid_size = int(len(full_train_dataset) * VALID_RATIO)
    # 학습 데이터 개수를 계산합니다.
    train_size = len(full_train_dataset) - valid_size
    # 재현 가능한 분할을 위해 torch Generator에 시드를 설정합니다.
    generator = torch.Generator().manual_seed(SEED)
    # 전체 학습 데이터셋을 학습용과 검증용으로 나눕니다.
    train_dataset, valid_dataset = random_split(full_train_dataset, [train_size, valid_size], generator=generator)
    # 학습 DataLoader는 데이터를 섞어서 미니배치를 구성합니다.
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    # 검증 DataLoader는 성능 평가용이므로 순서를 섞지 않습니다.
    valid_loader = DataLoader(valid_dataset, batch_size=batch_size, shuffle=False)
    # 테스트 DataLoader는 최종 평가용이므로 순서를 섞지 않습니다.
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    # 세 가지 DataLoader를 반환합니다.
    return train_loader, valid_loader, test_loader
