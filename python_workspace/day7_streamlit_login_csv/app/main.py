from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
print('BASE_DIR: ', BASE_DIR)

USER_CSV_PATH = BASE_DIR / "data" / "users.csv"

st.set_page_config(
    layout="wide",
    page_icon="📊",
    page_title="Streamlit Login",
    initial_sidebar_state="expanded",
)

def init_session_state() -> None:
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'user_email' not in st.session_state:
        st.session_state.user_email = None
    if 'user_name' not in st.session_state:
        st.session_state.user_name = None
    if 'show_login_error' not in st.session_state:
        st.session_state.show_login_error = False

@st.cache_data #csv 파일을 매번 새로 읽을 필요가 없음.
def load_users() ->pd.DataFrame:
    if not USER_CSV_PATH.exists():
        st.error(f'사용자 csv 파일이 없습니다 :', {USER_CSV_PATH})
        st.stop()

    user_df = pd.read_csv(USER_CSV_PATH)
    required_columns = {'email', 'password', 'name'}
    if not required_columns.issubset(user_df.columns):
        st.error(f'사용자 csv 파일의 열 이름이 맞지 않습니다 :', {required_columns})
        st.stop()
    
    user_df['email'] = user_df['email'].astype(str)
    user_df['password'] = user_df['password'].astype(str)
    user_df['name'] = user_df['name'].astype(str)
    return user_df

def check_login(email: str, password: str) -> tuple[bool, str]:
    users_df = load_users()

    email = email.strip()
    password = password.strip()

    matched = users_df[
        (users_df['email'] == email) &
        (users_df['password'] == password)
    ]

    if not matched.empty:
        return True, matched.iloc[0]['name']

    return False, ""

@st.dialog('로그인 실패')
def login_error_dialog() -> None:
    st.error('아이디와 비밀번호를 확인해주세요')
    if st.button('닫기'):
        st.session_state.show_login_error = False
        st.rerun()



def show_login_page() -> None:
    st.title('로그인')

    with st.form('login_form'):
        email = st.text_input('아이디', placeholder='admin@example.com')
        password = st.text_input('비밀번호', type='password')
        submitted = st.form_submit_button('로그인')

    if submitted:
        success, user_name = check_login(email, password)

        if success:
            st.session_state.logged_in = True
            st.session_state.user_name = user_name
            st.session_state.user_email = email.strip()
            st.session_state.show_login_error = False
            st.rerun()
        else:
            st.session_state.show_login_error = True

    if st.session_state.show_login_error:
        login_error_dialog()

def main() -> None:
    init_session_state()
    if st.session_state.logged_in:
        show_dashboard_page()
    else:
        show_login_page()


def read_upload_csv(uploaded_file) -> pd.DataFrame:
    try:
        return pd.read_csv(uploaded_file)
    except UnicodeDecodeError:
        uploaded_file.seek(0)
        return pd.read_csv(uploaded_file, encoding='cp949')
    except Exception as e:
        st.error(f'업로드한 파일이 손상되었습니다. 이미지 파일만 업로드 할 수 있습니다.')
        st.stop()


def show_dashboard_page() -> None:
    st.title('csv 데이터 분석')
    if not st.session_state.logged_in:
        st.stop()
    
    user_df = load_users()
    user = user_df[user_df['email'] == st.session_state.user_email]
    
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write(f'{st.session_state.user_name}님, 안녕하세요.')
    with col2:
        if st.button('로그아웃'):
            st.session_state.logged_in = False
            st.session_state.user_email = None
            st.session_state.user_name = None
            st.session_state.show_login_error = False
            st.rerun()

    st.divider()
    uploaded_file = st.file_uploader('파일 업로드', type=['csv'], help='data/sample_sales.csv 파일을 업로드해주세요.')
    if uploaded_file is None:
        st.info('csv 파일을 업로드하면 테이블과 기본통계, 선, 막대그래프, 히스토그램이 출력됩니다.')
        st.write('프로젝트예제 데이터파일 data/sample_sales.csv')
        return
    
    st.subheader('읽어온 데이터 테이블')
    df = read_upload_csv(uploaded_file)
    st.dataframe(df, use_container_width=True)
    
    st.subheader('기본 데이터 정보')
    col1, col2, col3 = st.columns([1, 1, 2])
    col1.metric('행 갯수', len(df))
    col2.metric('열 갯수', len(df.columns))
    col3.metric('결측치', int(df.isna().sum().sum()))

    st.subheader('통계요약')
    numeric_df = df.select_dtypes(include=['number'])
    if numeric_df.empty:
        st.write('숫자 형식의 데이터가 없습니다.')
        return
    st.dataframe(numeric_df.describe(), use_container_width=True)
    
    st.subheader('통계 그래프')
    selected_columns = st.selectbox('그래프로 보여줄 컬럼', numeric_df.columns)
    chart_type = st.radio('그래프 타입', ['line', 'bar', 'histogram'], horizontal=True)
    if chart_type == 'line':
        st.line_chart(numeric_df[selected_columns])
    elif chart_type == 'bar':
        st.bar_chart(numeric_df[selected_columns])
    elif chart_type == 'histogram':
        fig, ax = plt.subplots()
        ax.hist(numeric_df[selected_columns].dropna(), bins=10)
        ax.set_title(f'{selected_columns} Histogram')
        ax.set_xlabel(selected_columns)
        ax.set_ylabel('Frequency')
        st.pyplot(fig)



    with col1:
        st.write('테이블 전체 개수')
        st.write(df.shape[0])
    with col2:
        st.write('테이블 전체 컬럼 개수')
        st.write(df.shape[1])
    with col3:
        st.write('테이블 전체 데이터 개수')        
        st.write(df.shape[0] * df.shape[1])


if __name__ == '__main__':
    main()

    #admin@example.com