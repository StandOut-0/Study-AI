"""네이버 영화 리뷰 감성 분류 Transformer 모델을 학습하는 실행 파일입니다."""

# argparse는 터미널에서 epoch, batch size 같은 옵션을 받을 때 사용합니다.
import argparse

# random은 파이썬 기본 난수 시드를 고정하기 위해 사용합니다.
import random

# numpy는 NumPy 난수 시드를 고정하기 위해 사용합니다.
import numpy as np

# torch는 모델 학습과 텐서 연산을 위해 사용합니다.
import torch

# nn은 손실 함수를 사용하기 위해 불러옵니다.
from torch import nn

# tqdm은 학습 진행률을 보기 좋게 출력하기 위해 사용합니다.
from tqdm import tqdm

# 프로젝트 설정값을 가져옵니다.
from src.config import MAX_LEN, VOCAB_SIZE, BATCH_SIZE, D_MODEL, N_HEADS, N_LAYERS, FF_DIM, DROPOUT, LEARNING_RATE, EPOCHS, SEED, MODEL_PATH, VOCAB_PATH, CHECKPOINT_DIR, TRAIN_FILE

# NSMC 데이터 다운로드와 DataLoader 생성 함수를 가져옵니다.
from src.data import ensure_nsmc_downloaded, load_nsmc, create_dataloaders

# Vocabulary 클래스는 학습 데이터 기반 단어 사전을 만들기 위해 사용합니다.
from src.tokenizer import Vocabulary

# Transformer 감성 분류 모델 클래스를 가져옵니다.
from src.model import NaverTransformerSentiment


# set_seed 함수는 실행할 때마다 최대한 같은 결과가 나오도록 난수 시드를 고정합니다.
def set_seed(seed: int) -> None:
    # 파이썬 random 모듈의 난수 시드를 고정합니다.
    random.seed(seed)
    # NumPy 난수 시드를 고정합니다.
    np.random.seed(seed)
    # PyTorch CPU 난수 시드를 고정합니다.
    torch.manual_seed(seed)
    # CUDA 사용 가능 시 GPU 난수 시드도 고정합니다.
    torch.cuda.manual_seed_all(seed)


# train_one_epoch 함수는 모델을 한 epoch 동안 학습합니다.
def train_one_epoch(model, loader, criterion, optimizer, device):
    # 모델을 학습 모드로 전환하여 Dropout이 학습 방식으로 동작하게 합니다.
    model.train()
    # 누적 손실값을 저장할 변수를 초기화합니다.
    total_loss = 0.0
    # 맞힌 샘플 수를 저장할 변수를 초기화합니다.
    total_correct = 0
    # 전체 샘플 수를 저장할 변수를 초기화합니다.
    total_count = 0
    # DataLoader에서 미니배치를 하나씩 가져옵니다.
    for x, y in tqdm(loader, desc="train", leave=False):
        # 입력 토큰 ID 텐서를 학습 장치로 이동합니다.
        x = x.to(device)
        # 정답 레이블 텐서를 학습 장치로 이동합니다.
        y = y.to(device)
        # 이전 미니배치에서 계산된 기울기를 초기화합니다.
        optimizer.zero_grad()
        # 모델에 입력을 넣어 클래스별 로짓을 계산합니다.
        logits = model(x)
        # 로짓과 정답 레이블을 비교하여 손실을 계산합니다.
        loss = criterion(logits, y)
        # 손실을 기준으로 역전파를 수행하여 기울기를 계산합니다.
        loss.backward()
        # 계산된 기울기를 이용해 모델 파라미터를 업데이트합니다.
        optimizer.step()
        # 현재 미니배치 손실에 샘플 수를 곱해 누적합니다.
        total_loss += loss.item() * x.size(0)
        # 가장 큰 로짓을 가진 클래스를 예측값으로 선택합니다.
        pred = torch.argmax(logits, dim=1)
        # 예측값과 정답이 같은 샘플 수를 누적합니다.
        total_correct += (pred == y).sum().item()
        # 현재 미니배치 샘플 수를 누적합니다.
        total_count += x.size(0)
    # 평균 손실과 정확도를 계산하여 반환합니다.
    return total_loss / total_count, total_correct / total_count


# evaluate 함수는 검증/테스트 데이터에 대한 손실과 정확도를 계산합니다.
def evaluate(model, loader, criterion, device):
    # 모델을 평가 모드로 전환하여 Dropout이 비활성화되게 합니다.
    model.eval()
    # 누적 손실값을 저장할 변수를 초기화합니다.
    total_loss = 0.0
    # 맞힌 샘플 수를 저장할 변수를 초기화합니다.
    total_correct = 0
    # 전체 샘플 수를 저장할 변수를 초기화합니다.
    total_count = 0
    # 평가에서는 기울기를 계산하지 않아 메모리와 시간을 줄입니다.
    with torch.no_grad():
        # DataLoader에서 미니배치를 하나씩 가져옵니다.
        for x, y in tqdm(loader, desc="eval", leave=False):
            # 입력 토큰 ID 텐서를 평가 장치로 이동합니다.
            x = x.to(device)
            # 정답 레이블 텐서를 평가 장치로 이동합니다.
            y = y.to(device)
            # 모델에 입력을 넣어 클래스별 로짓을 계산합니다.
            logits = model(x)
            # 로짓과 정답 레이블을 비교하여 손실을 계산합니다.
            loss = criterion(logits, y)
            # 현재 미니배치 손실에 샘플 수를 곱해 누적합니다.
            total_loss += loss.item() * x.size(0)
            # 가장 큰 로짓을 가진 클래스를 예측값으로 선택합니다.
            pred = torch.argmax(logits, dim=1)
            # 예측값과 정답이 같은 샘플 수를 누적합니다.
            total_correct += (pred == y).sum().item()
            # 현재 미니배치 샘플 수를 누적합니다.
            total_count += x.size(0)
    # 평균 손실과 정확도를 계산하여 반환합니다.
    return total_loss / total_count, total_correct / total_count


# main 함수는 데이터 준비, 모델 생성, 학습, 저장 과정을 순서대로 실행합니다.
def main():
    # 명령행 옵션을 처리할 ArgumentParser 객체를 생성합니다.
    parser = argparse.ArgumentParser(description="NSMC Transformer 감성 분류 모델 학습")
    # epoch 수를 터미널에서 변경할 수 있게 옵션을 추가합니다.
    parser.add_argument("--epochs", type=int, default=EPOCHS)
    # batch size를 터미널에서 변경할 수 있게 옵션을 추가합니다.
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE)
    # 최대 문장 길이를 터미널에서 변경할 수 있게 옵션을 추가합니다.
    parser.add_argument("--max-len", type=int, default=MAX_LEN)
    # 단어 사전 크기를 터미널에서 변경할 수 있게 옵션을 추가합니다.
    parser.add_argument("--vocab-size", type=int, default=VOCAB_SIZE)
    # 빠른 테스트용으로 학습 데이터 일부만 사용할 수 있게 옵션을 추가합니다.
    parser.add_argument("--sample-size", type=int, default=0, help="0이면 전체 데이터 사용, 양수이면 일부 샘플만 사용")
    # 터미널 입력 옵션을 파싱합니다.
    args = parser.parse_args()
    # 실험 재현성을 위해 난수 시드를 고정합니다.
    set_seed(SEED)
    # GPU가 있으면 cuda를 사용하고 없으면 cpu를 사용합니다.
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # 체크포인트 저장 폴더를 생성합니다.
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    # NSMC 데이터 파일을 다운로드합니다.
    ensure_nsmc_downloaded()
    # 학습 데이터를 DataFrame으로 읽습니다.
    train_df = load_nsmc(TRAIN_FILE)
    # sample_size가 양수이면 빠른 실습을 위해 일부 데이터만 사용합니다.
    if args.sample_size and args.sample_size > 0:
        # 지정한 샘플 수만큼 학습 데이터를 앞에서부터 선택합니다.
        train_df = train_df.iloc[: args.sample_size].copy()
    # 학습 리뷰 문장으로 단어 사전을 생성합니다.
    vocab = Vocabulary(max_size=args.vocab_size, min_freq=2)
    # 단어 사전에 학습 리뷰의 토큰 빈도를 반영합니다.
    vocab.build(train_df["document"].astype(str).tolist())
    # 생성된 단어 사전을 JSON 파일로 저장합니다.
    vocab.save(VOCAB_PATH)
    # 학습/검증/테스트 DataLoader를 생성합니다.
    train_loader, valid_loader, test_loader = create_dataloaders(vocab, args.max_len, args.batch_size, args.sample_size)
    # Transformer 감성 분류 모델을 생성합니다.
    model = NaverTransformerSentiment(len(vocab), args.max_len, D_MODEL, N_HEADS, N_LAYERS, FF_DIM, DROPOUT)
    # 모델을 CPU 또는 GPU 장치로 이동합니다.
    model = model.to(device)
    # 다중 클래스 분류에 적합한 CrossEntropyLoss를 손실 함수로 사용합니다.
    criterion = nn.CrossEntropyLoss()
    # AdamW는 Adam에 weight decay를 안정적으로 적용하는 최적화 함수입니다.
    optimizer = torch.optim.AdamW(model.parameters(), lr=LEARNING_RATE)
    # 가장 좋은 검증 정확도를 저장할 변수를 초기화합니다.
    best_valid_acc = 0.0
    # 지정한 epoch 수만큼 학습을 반복합니다.
    for epoch in range(1, args.epochs + 1):
        # 한 epoch 동안 학습을 수행하고 손실/정확도를 받습니다.
        train_loss, train_acc = train_one_epoch(model, train_loader, criterion, optimizer, device)
        # 검증 데이터로 현재 모델 성능을 평가합니다.
        valid_loss, valid_acc = evaluate(model, valid_loader, criterion, device)
        # 현재 epoch 결과를 화면에 출력합니다.
        print(f"Epoch {epoch}/{args.epochs} | train_loss={train_loss:.4f}, train_acc={train_acc:.4f}, valid_loss={valid_loss:.4f}, valid_acc={valid_acc:.4f}")
        # 검증 정확도가 기존 최고 정확도보다 높으면 모델을 저장합니다.
        if valid_acc > best_valid_acc:
            # 최고 검증 정확도를 갱신합니다.
            best_valid_acc = valid_acc
            # 모델 파라미터와 설정값을 체크포인트 파일로 저장합니다.
            torch.save({"model_state_dict": model.state_dict(), "max_len": args.max_len, "vocab_size": len(vocab)}, MODEL_PATH)
            # 저장 완료 메시지를 출력합니다.
            print(f"모델 저장 완료: {MODEL_PATH}")
    # 저장된 최고 모델 파라미터를 다시 불러옵니다.
    checkpoint = torch.load(MODEL_PATH, map_location=device)
    # 체크포인트의 파라미터를 현재 모델에 적용합니다.
    model.load_state_dict(checkpoint["model_state_dict"])
    # 테스트 데이터로 최종 성능을 평가합니다.
    test_loss, test_acc = evaluate(model, test_loader, criterion, device)
    # 최종 테스트 결과를 출력합니다.
    print(f"최종 테스트 결과 | test_loss={test_loss:.4f}, test_acc={test_acc:.4f}")


# 이 파일을 직접 실행할 때만 main 함수를 호출합니다.
if __name__ == "__main__":
    # 전체 학습 절차를 시작합니다.
    main()
