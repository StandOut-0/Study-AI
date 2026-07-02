"""학습된 Transformer 모델로 새로운 한국어 리뷰의 감성을 예측하는 파일입니다."""

# torch는 모델 로딩과 예측 연산에 사용합니다.
import torch

# 프로젝트 설정값을 가져옵니다.
from src.config import MODEL_PATH, VOCAB_PATH, MAX_LEN, D_MODEL, N_HEADS, N_LAYERS, FF_DIM, DROPOUT

# Transformer 감성 분류 모델 클래스를 가져옵니다.
from src.model import NaverTransformerSentiment

# 저장된 단어 사전을 불러오기 위해 Vocabulary 클래스를 가져옵니다.
from src.tokenizer import Vocabulary


# load_model_and_vocab 함수는 저장된 단어 사전과 모델을 함께 불러옵니다.
def load_model_and_vocab(device: torch.device | None = None):
    # device가 전달되지 않으면 GPU 가능 여부에 따라 자동으로 선택합니다.
    device = device or torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # 단어 사전 파일이 없으면 학습을 먼저 실행해야 하므로 오류를 발생시킵니다.
    if not VOCAB_PATH.exists() or not MODEL_PATH.exists():
        # 사용자에게 학습 명령을 안내하는 오류 메시지를 제공합니다.
        raise FileNotFoundError("모델 파일이 없습니다. 먼저 `python -m src.train` 명령으로 학습을 실행하세요.")
    # JSON 파일에서 단어 사전을 복원합니다.
    vocab = Vocabulary.load(VOCAB_PATH)
    # 저장된 모델 체크포인트를 지정 장치 기준으로 읽습니다.
    checkpoint = torch.load(MODEL_PATH, map_location=device)
    # 체크포인트에 저장된 최대 길이를 우선 사용하고 없으면 설정값을 사용합니다.
    max_len = int(checkpoint.get("max_len", MAX_LEN))
    # 단어 사전 크기와 저장된 설정으로 모델 구조를 생성합니다.
    model = NaverTransformerSentiment(len(vocab), max_len, D_MODEL, N_HEADS, N_LAYERS, FF_DIM, DROPOUT)
    # 체크포인트의 학습된 파라미터를 모델에 적용합니다.
    model.load_state_dict(checkpoint["model_state_dict"])
    # 모델을 예측 장치로 이동합니다.
    model = model.to(device)
    # 모델을 평가 모드로 전환합니다.
    model.eval()
    # 모델, 단어 사전, 최대 길이, 장치를 반환합니다.
    return model, vocab, max_len, device


# predict_sentiment 함수는 리뷰 문장 하나를 받아 감성 라벨과 확률을 반환합니다.
def predict_sentiment(text: str, model, vocab: Vocabulary, max_len: int, device: torch.device):
    # 입력 문장을 학습 때와 같은 방식으로 정수 ID 리스트로 변환합니다.
    ids = vocab.encode(text, max_len)
    # 정수 ID 리스트를 배치 차원이 있는 LongTensor로 변환합니다.
    x = torch.tensor([ids], dtype=torch.long).to(device)
    # 예측 과정에서는 기울기 계산이 필요 없으므로 비활성화합니다.
    with torch.no_grad():
        # 모델에 입력을 넣어 클래스별 로짓을 계산합니다.
        logits = model(x)
        # softmax를 적용해 클래스별 확률로 변환합니다.
        probs = torch.softmax(logits, dim=1).squeeze(0)
        # 가장 높은 확률의 클래스 ID를 선택합니다.
        pred_id = int(torch.argmax(probs).item())
    # 클래스 ID가 1이면 긍정, 0이면 부정으로 해석합니다.
    label = "긍정" if pred_id == 1 else "부정"
    # 긍정 클래스 확률을 실수로 추출합니다.
    positive_prob = float(probs[1].item())
    # 부정 클래스 확률을 실수로 추출합니다.
    negative_prob = float(probs[0].item())
    # 예측 결과를 딕셔너리로 반환합니다.
    return {"label": label, "positive_prob": positive_prob, "negative_prob": negative_prob}
