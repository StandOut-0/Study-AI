# 네이버 영화 리뷰 Transformer 감성 분류 Streamlit 프로젝트

이 프로젝트는 제공된 Transformer 실습 코드의 핵심 구조인 Self-Attention, Transformer Block, Word Embedding, Positional Embedding, 평균 풀링 분류 구조를 바탕으로 작성한 PyTorch 기반 한국어 감성 분류 앱입니다.

## 기능

- NSMC 네이버 영화 리뷰 데이터 자동 다운로드
- 한국어 리뷰 문장 전처리 및 단어 사전 생성
- Transformer Encoder 기반 긍정/부정 감성 분류 모델 학습
- 학습된 모델 저장
- Streamlit 화면에서 한국어 리뷰 문장 감성 예측

## 프로젝트 구조

```text
naver_transformer_sentiment_project/
├─ app/
│  └─ streamlit_app.py
├─ src/
│  ├─ config.py
│  ├─ data.py
│  ├─ tokenizer.py
│  ├─ model.py
│  ├─ train.py
│  └─ predict.py
├─ data/
│  └─ raw/
├─ checkpoints/
├─ requirements.txt
├─ .gitignore
└─ README.md
```

## PyCharm 실행 순서



python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

### 1. 프로젝트 열기

PyCharm에서 이 폴더를 Open 합니다.

### 2. 가상환경 생성

Python 3.10 또는 3.11 가상환경을 권장합니다.

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 모델 학습

처음 실행 시에는 모델 파일이 없으므로 반드시 학습을 먼저 실행합니다.

```bash
python -m src.train --epochs 3
```

빠르게 동작만 확인하려면 일부 샘플만 학습할 수 있습니다.

```bash
python -m src.train --epochs 1 --sample-size 5000
```

### 5. Streamlit 앱 실행

```bash
streamlit run app/streamlit_app.py
```

## 예시 입력

```text
배우들의 연기가 좋고 스토리가 감동적이었어요.
```

```text
스토리가 지루하고 시간이 아까웠어요.
```

## 주의사항

- 처음 학습할 때 NSMC 데이터가 GitHub에서 다운로드됩니다.
- 회사/학교 네트워크에서 GitHub 접속이 차단되어 있으면 `data/raw` 폴더에 `ratings_train.txt`, `ratings_test.txt`를 직접 넣으면 됩니다.
- CPU에서도 실행 가능하지만 전체 데이터 학습은 시간이 걸릴 수 있습니다.
