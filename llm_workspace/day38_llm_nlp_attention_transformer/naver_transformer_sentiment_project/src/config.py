"""프로젝트 전체에서 공통으로 사용할 설정값을 모아 둔 파일입니다."""

# pathlib.Path는 운영체제별 경로 구분자 차이를 자동으로 처리하기 위해 사용합니다.
from pathlib import Path

# 현재 config.py 파일의 위치에서 부모 폴더를 두 번 올라가 프로젝트 루트 경로를 계산합니다.
BASE_DIR = Path(__file__).resolve().parents[1]

# 원본 NSMC 데이터 파일을 저장할 폴더 경로를 지정합니다.
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

# 학습된 모델과 단어 사전 파일을 저장할 폴더 경로를 지정합니다.
CHECKPOINT_DIR = BASE_DIR / "checkpoints"

# NSMC 학습 데이터 파일을 저장할 전체 경로를 지정합니다.
TRAIN_FILE = RAW_DATA_DIR / "ratings_train.txt"

# NSMC 테스트 데이터 파일을 저장할 전체 경로를 지정합니다.
TEST_FILE = RAW_DATA_DIR / "ratings_test.txt"

# 학습된 Transformer 모델 파라미터를 저장할 파일 경로를 지정합니다.
MODEL_PATH = CHECKPOINT_DIR / "naver_transformer_sentiment.pt"

# 학습 데이터에서 만든 단어 사전 파일을 저장할 경로를 지정합니다.
VOCAB_PATH = CHECKPOINT_DIR / "vocab.json"

# NSMC 학습 데이터 다운로드 URL을 지정합니다.
TRAIN_URL = "https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt"

# NSMC 테스트 데이터 다운로드 URL을 지정합니다.
TEST_URL = "https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt"

# 문장을 토큰 ID 시퀀스로 변환할 때 사용할 최대 토큰 길이를 지정합니다.
MAX_LEN = 64

# 단어 사전에 등록할 최대 토큰 개수를 지정합니다.
VOCAB_SIZE = 30000

# 한 번의 학습 단계에서 사용할 리뷰 개수를 지정합니다.
BATCH_SIZE = 64

# Transformer 내부 임베딩 벡터 차원을 지정합니다.
D_MODEL = 128

# Multi-Head Self-Attention에서 사용할 head 개수를 지정합니다.
N_HEADS = 4

# Transformer Encoder Block을 몇 층 쌓을지 지정합니다.
N_LAYERS = 2

# Feed Forward Network의 중간 차원을 지정합니다.
FF_DIM = 256

# 과적합을 줄이기 위해 사용할 Dropout 비율을 지정합니다.
DROPOUT = 0.1

# 모델 학습률을 지정합니다.
LEARNING_RATE = 1e-4

# 기본 학습 epoch 수를 지정합니다.
EPOCHS = 3

# 학습/검증 분할에서 검증 데이터 비율을 지정합니다.
VALID_RATIO = 0.1

# 재현 가능한 실험을 위해 난수 시드를 지정합니다.
SEED = 42
