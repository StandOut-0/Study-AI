import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sanghee", page_icon="📊", layout="wide")
plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False

# st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=80)

st.markdown("""
    <style>
    div.stButton > button { 
        background-color: #007BFF; 
        color: white; 
        border-radius: 8px; 
    }
    div[data-testid="stSlider"], 
    div[data-testid="stRadio"], 
    div[data-testid="stTextInput"], 
    div[data-testid="stSelectbox"],
    div[data-testid="stTextArea"]{
        display: flex;
        flex-direction: row;
        align-items: center; 
        gap: 15px;
        margin-bottom: 10px;
    }
    div[data-testid="stSlider"] label, 
    div[data-testid="stRadio"] label, 
    div[data-testid="stTextInput"] label, 
    div[data-testid="stSelectbox"] label,
    div[data-testid="stTextArea"] label{
        min-width: 70px;
        margin-bottom: 0 !important;
        font-weight: bold;
        white-space: nowrap; 
    }
</style>
    """, unsafe_allow_html=True)

head_col1, head_col2 = st.columns([2, 3], gap="large")

with head_col1:
    st.markdown('<h1 style="font-size:70px;">📊</h1>', unsafe_allow_html=True)
    st.title("Streamlit GUI 예제")
    st.divider()

    row1 = st.container()
    row2 = st.container()

    with row1:
        st.subheader("Streamlit 입력 예제")
        inner_col1, inner_col2 = st.columns([1, 1], gap="small")

        with inner_col1:
            gender = st.radio("성별", ("남자", "여자"), horizontal=True)
            name = st.text_input("이름")
            country = st.selectbox("국가", ("한국", "중국", "유럽")) 
        with inner_col2:
            
            python_score = st.slider("Python 점수", 0, 100)
            sql_score = st.slider("SQL 점수", 0, 100)
            ai_score = st.slider("AI 점수", 0, 100)
    
        text = st.text_area("메모", height=30)
        uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.success("파일 업로드 성공")
            st.write("### 데이터 미리보기")
            st.dataframe(df, use_container_width=True)
            st.write("### 기본 통계")
            st.write(df.describe())
        else:
            st.info("아직 파일이 업로드되지 않았습니다.")

        agree = st.checkbox("데이터활용에 동의합니다.")


    with row2:
        if st.button("학습 결과 분석"):
            if name.strip() == "":
                st.write("이름을 입력해주세요.")
            elif python_score < 0:
                st.write("Python 점수를 입력해주세요.")
            elif sql_score < 0:
                st.write("SQL 점수를 입력해주세요.")
            elif ai_score < 0:
                st.write("AI 점수를 입력해주세요.")
            elif agree == False:
                st.write("데이터활용에 동의해주세요.")
            elif country == "":
                st.write("국가를 입력해주세요.")
            else:
                scores = { 
                    "과목": ["Python", "SQL", "AI"], 
                    "점수": [python_score, sql_score, ai_score] 
                }
                df = pd.DataFrame(scores) 
                avg_score = df["점수"].mean()

                st.divider()
                
                st.subheader("1. 학습자 정보") 
                st.write(f"이름: {name}") 
                st.write(f"성별: {gender}") 
                st.write(f"국가: {country}") 
                st.write(f"메모: {text}") 
                st.subheader("2. 학습 결과") 
                st.write(f"평균 점수: {avg_score:.2f}") 
                



with head_col2:
    row1 = st.container()
    row2 = st.container()

    df = pd.DataFrame({
        "과목": ["Python", "SQL", "AI"],
        "점수": [python_score, sql_score, ai_score]
    })

    with row1:
        st.subheader("학습 결과 상세 분석")
        inner_col1, inner_col2 = st.columns([1, 1], gap="small")
        inner_col1, inner_col2 = st.columns([1, 1], gap="small")

        with inner_col1:
            st.text("data 요약")
            st.write(df.describe())

        with inner_col2:
            st.text("data 시각화")
            st.dataframe(df, use_container_width=True)

            

    with row2:
        colors = ['#3898e7', '#8fe279', '#e53678']
        inner_col1, inner_col2 = st.columns([1, 1], gap="small")
        fig, ax = plt.subplots(figsize=(6, 2.5))

        ax.bar(df[df.columns[0]], df[df.columns[1]], color=colors)

        ax.set_title("matplotlib.pyplot subplots")
        ax.set_xlabel("subject")
        ax.set_ylabel("score")

        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)

        with inner_col1:
            st.text("data 컬러 정렬만 바꿔보기")
            st.pyplot(fig)

        with inner_col2:
            st.text("data 컬러 정렬만 바꿔보기")
            st.pyplot(fig)