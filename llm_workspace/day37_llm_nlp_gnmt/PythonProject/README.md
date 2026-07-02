


# Torch 기반 스마트 번역기 Streamlit 프로젝트
## [UPDATE] 260702 - Seq2Seq를 Transformer로 대체하기 

## 결과
<img width="1004" height="505" alt="image" src="https://github.com/user-attachments/assets/d7054ef6-c88e-4514-bcfa-313b389b8ad0" />
<img width="873" height="779" alt="image" src="https://github.com/user-attachments/assets/f3a8f8b6-bf30-4801-8caf-fa105e168b66" />
<BR><BR><BR><BR><BR><BR>

## 과정

[STUDY] Day38 - NLP - GPT - day37_PythonProject - config

1. Transformer는 hidden개념이 없다. 삭제.
HIDDEN_SIZE = 128

2. Transformer용 파라미터 추가
Transformer 모델 차원
D_MODEL = 64   # EMBED_SIZE와 보통 동일하게 맞춤

Multi-Head Attention 개수
N_HEADS = 8

Encoder / Decoder layer 수
NUM_LAYERS = 3

Dropout (과적합 방지)
DROPOUT = 0.1

3. EMBED_SIZE는 통합한다.
EMBED_SIZE = 64
EMBED_SIZE = D_MODEL
<img width="1467" height="964" alt="image" src="https://github.com/user-attachments/assets/fbed5d19-73a4-4f6a-8170-fb29b1293ddc" />
<BR><BR><BR><BR><BR><BR>


[STUDY] Day38 - NLP - GPT - day37_PythonProject - model.py
0. from src.config import EMBED_SIZE, HIDDEN_SIZE히든 삭제
1. 기존 코드를 모두 지워야함 새로구현.
<img width="1080" height="1880" alt="image" src="https://github.com/user-attachments/assets/bc287ad8-e235-4ad5-b481-e3d61790d6a8" />
<BR><BR><BR><BR><BR><BR>


[STUDY] Day38 - NLP - GPT - day37_PythonProject - train.py
1.   모델생성 수정
    # model = Seq2SeqTranslator(vocab_size, EMBED_SIZE, HIDDEN_SIZE).to(device)
    model = Seq2SeqTranslator(
        vocab_size=vocab_size,
        d_model=EMBED_SIZE,
        n_heads=8,
        num_layers=3,
        dropout=0.1
    ).to(device)
3.  forward 호출 변경
            # logits = model(source_idx, decoder_input_idx)
            tgt_mask = nn.Transformer.generate_square_subsequent_mask(
                decoder_input_idx.size(1)
            ).to(device)

            logits = model(
                source_idx,
                decoder_input_idx,
                tgt_mask
            )
4.   HIDDEN_SIZE히든 삭제
    torch.save({
        "char2idx": char2idx,
        "idx2char": idx2char,
        "embed_size": EMBED_SIZE
        # "hidden_size": HIDDEN_SIZE,
    }, META_PATH)


<img width="1080" height="1880" alt="image" src="https://github.com/user-attachments/assets/8e0b2c37-1e37-4a2f-9403-8090d8aa098c" />
<BR><BR><BR><BR><BR><BR>


[STUDY] Day38 - NLP - GPT - day37_PythonProject - predict.py
1. 기존 코드를 모두 지워야함 새로구현.
<img width="1080" height="1880" alt="image" src="https://github.com/user-attachments/assets/4d827de8-3d82-412b-8793-cc3135848daa" />
<BR><BR><BR><BR><BR><BR>
<BR><BR><BR><BR><BR><BR>





# BEFORE HISTORY

핵심 흐름은 다음과 같습니다.

- 번역 데이터 구축
- 문자 사전 생성
- 인코더 입력, 디코더 입력, 디코더 출력 데이터 구성
- Seq2Seq RNN 모델 구현
- 손실 함수와 옵티마이저를 이용한 지도 학습
- 학습된 모델로 새 문장 번역
- 반복 학습 수, 최적화 함수, 손실 함수, RNN 은닉 차원 등을 조절하는 최적화

## 프로젝트 구조
```text
smart_translator_torch_streamlit_project/
├─ app/
│  └─ streamlit_app.py
├─ data/
│  └─ translation_pairs.csv
├─ models/
├─ src/
│  ├─ config.py
│  ├─ data_utils.py
│  ├─ model.py
│  ├─ predict.py
│  └─ train.py
├─ .gitignore
├─ README.md
└─ requirements.txt
```

## 설치
```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install setuptools==81.0.0
pip install -r requirements.txt
```

## 모델 학습
```bash
python -m src.train
```

학습이 완료되면 다음 파일이 생성됩니다.
```text
models/smart_translator.pt
models/translator_meta.pt
```

## Streamlit 실행
```bash
streamlit run app/streamlit_app.py
```

## 사용 예시
영어 입력:
```text
hello
thank you
i am a student
what are you doing
```

한국어 입력:
```text
안녕하세요
감사합니다
나는 학생입니다
무엇을 하고 있나요
```

## 참고
이 예제는  문자 단위 Seq2Seq 모델입니다. 
실제 상용 번역기 수준의 품질을 원한다면 더 많은 병렬 말뭉치, Transformer 기반 모델, SentencePiece 토크나이저, BLEU/chrF 평가 등을 추가해야 합니다.
