"""Streamlit 화면에서 한국어 영화 리뷰 감성을 예측하는 앱입니다."""

# sys는 src 폴더를 import 경로에 추가하기 위해 사용합니다.
import sys

# Path는 프로젝트 루트 경로를 계산하기 위해 사용합니다.
from pathlib import Path

# streamlit은 웹 화면을 구성하기 위해 사용합니다.
import streamlit as st

# torch는 CPU/GPU 장치 선택에 사용합니다.
import torch

# 현재 파일 기준으로 프로젝트 루트 경로를 계산합니다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# 프로젝트 루트 경로를 파이썬 import 검색 경로에 추가합니다.
sys.path.append(str(PROJECT_ROOT))

# 학습된 모델과 단어 사전을 불러오는 함수를 가져옵니다.
from src.predict import load_model_and_vocab, predict_sentiment


# load_resource 함수는 Streamlit 캐시를 사용해 모델을 한 번만 로딩합니다.
@st.cache_resource
# 캐시된 모델/단어 사전/설정값을 반환하는 함수를 정의합니다.
def load_resource():
    # GPU가 있으면 cuda, 없으면 cpu를 사용하도록 장치를 선택합니다.
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # 저장된 모델, 단어 사전, 최대 길이, 장치를 불러옵니다.
    model, vocab, max_len, device = load_model_and_vocab(device)
    # 로딩된 객체들을 반환합니다.
    return model, vocab, max_len, device


# main 함수는 Streamlit 화면 전체를 구성합니다.
def main():
    # Streamlit 페이지 제목, 아이콘, 화면 폭을 설정합니다.
    st.set_page_config(page_title="네이버 영화 리뷰 감성 분류", page_icon="🎬", layout="centered")
    # 앱의 큰 제목을 출력합니다.
    st.title("🎬 네이버 영화 리뷰 감성 분류")
    # 앱의 간단한 설명 문장을 출력합니다.
    st.write("한국어 영화 리뷰 문장을 입력하면 Transformer 모델이 긍정/부정을 예측합니다.")
    # 구분선을 출력하여 화면 영역을 나눕니다.
    st.divider()
    # 모델 파일이 없을 때 보여 줄 안내 문장을 미리 준비합니다.
    train_help = "모델이 없으면 PyCharm 터미널에서 `python -m src.train --epochs 3` 명령을 먼저 실행하세요."
    # 사용자가 리뷰 문장을 입력할 수 있는 큰 텍스트 입력창을 만듭니다.
    review_text = st.text_area("리뷰 문장 입력", value="배우들의 연기가 좋고 스토리가 감동적이었어요.", height=140)
    # 예측 실행 버튼을 만듭니다.
    clicked = st.button("감성 예측하기", type="primary")
    # 버튼이 클릭되었을 때만 예측을 수행합니다.
    if clicked:
        # 입력 문장이 비어 있으면 경고 메시지를 출력합니다.
        if not review_text.strip():
            # 빈 입력에 대한 사용자 안내를 표시합니다.
            st.warning("리뷰 문장을 입력하세요.")
            # 이후 예측 로직을 실행하지 않기 위해 함수를 종료합니다.
            return
        # 모델 로딩 또는 예측 중 오류가 날 수 있으므로 예외 처리를 사용합니다.
        try:
            # 캐시된 모델과 단어 사전을 불러옵니다.
            model, vocab, max_len, device = load_resource()
            # 입력 리뷰에 대한 감성 예측을 수행합니다.
            result = predict_sentiment(review_text, model, vocab, max_len, device)
            # 예측 결과 라벨을 큰 글씨로 출력합니다.
            st.subheader(f"예측 결과: {result['label']}")
            # 긍정 확률을 progress bar로 표시합니다.
            st.progress(result["positive_prob"], text=f"긍정 확률: {result['positive_prob']:.2%}")
            # 부정 확률을 progress bar로 표시합니다.
            st.progress(result["negative_prob"], text=f"부정 확률: {result['negative_prob']:.2%}")
            # 현재 모델이 실행된 장치 정보를 출력합니다.
            st.caption(f"실행 장치: {device}")
        # 모델 파일이 없을 때 발생하는 오류를 처리합니다.
        except FileNotFoundError as error:
            # 모델 학습이 필요하다는 오류 메시지를 출력합니다.
            st.error(str(error))
            # 학습 명령 안내 문장을 출력합니다.
            st.info(train_help)
        # 그 외 예상하지 못한 오류를 처리합니다.
        except Exception as error:
            # 오류 내용을 화면에 표시합니다.
            st.error(f"예측 중 오류가 발생했습니다: {error}")
            # 학습 명령 안내 문장을 함께 출력합니다.
            st.info(train_help)
    # 화면 하단에 학습 명령을 안내합니다.
    with st.expander("학습 실행 방법 보기"):
        # PyCharm 터미널에서 실행할 명령을 코드 블록으로 표시합니다.
        st.code("pip install -r requirements.txt\npython -m src.train --epochs 3\nstreamlit run app/streamlit_app.py", language="bash")


# 이 파일을 직접 실행할 때만 main 함수를 호출합니다.
if __name__ == "__main__":
    # Streamlit 앱 화면을 실행합니다.
    main()
