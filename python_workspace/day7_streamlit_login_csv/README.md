# streamlist 사용 로그인 기능과 csv 파일 업로드 및 데이터 분석 예제

# 로그인을 위한 테스트 데이터
email,password,name
admin@example.com,1234,관리자
student@example.com,pass123,수강생
teacher@example.com,teach123,강사

# 프로젝트 구조
streamlit_login_csv_project
├──.venv
├── app
│   ├── main.py
├── data
│   ├── sample_sales.csv
│   └── users.csv.zip
├── requirements.txt
└── README.md

# 기능
로그인 계정은 data/users.csv 파일에 저장되어 있습니다.
로그인 실패시 팝업에 알림이 나타납니다.
닫기버튼 누르면 다시 로그인 페이지로 이동합니다.
로그인 성공후에 csv파일 업로드하면 데이터테이블, 기본통계, 선, 막대그래프, 히스토그램 출력함

# 배포방법
깃허브에 프로젝트 업로드한 뒤 streamlit community cloud에서 새 앱 만들고 실행파일을 업로드함


# 실행방법
1. 프로젝트 폴더 생성
2. 가상환경 만들기
    - 아래 코드를 실행하여 가상환경 만들기
        - python -m venv .\.venv
        - .\.venv\Scripts\Activate.ps1
        - pip install -r requirements.txt
3. 실행
    - 아래 코드를 실행하여 실행
        - streamlit run app.py