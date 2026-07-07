# FastAPI ChatGPT 챗봇 앱 프로젝트

제공된 React 챗봇 예제를 참고하여 FastAPI 백엔드와 순수 HTML/CSS/JavaScript 화면으로 다시 작성한 ChatGPT 챗봇 프로젝트입니다.<br><br><br>

## 실습 [STUDY] Day39 - chatbot - 이전대화기록을 포함하고 설정값 지정할수있도록하기 
<img width="1078" height="814" alt="image" src="https://github.com/user-attachments/assets/07113885-417e-4ad5-8ec5-96cbbd2fd993" />

main에 설정값 instruction등을 추가했다.
<img width="1323" height="886" alt="image" src="https://github.com/user-attachments/assets/88d385d1-9bfe-4212-a102-ee158b42d947" />


schemas와 servce.py에 설정값 instruction등을 추가했다.
<img width="1323" height="886" alt="image" src="https://github.com/user-attachments/assets/92b324e5-b1ef-4e7b-86bb-d4b9133d6a65" />

<img width="1323" height="1013" alt="image" src="https://github.com/user-attachments/assets/e57f8462-6430-4046-a2b8-1c799d43aefb" />



js에 변수를 더 추가해 돌아가도록 한뒤 간단히 css를 추가했다 .
<img width="1323" height="1013" alt="image" src="https://github.com/user-attachments/assets/248f1037-6ccc-4eac-a918-f24df621e459" />

<img width="1323" height="1013" alt="image" src="https://github.com/user-attachments/assets/8dcaeea4-bdce-4f49-8319-6dbcf58ed208" />


<br><br><br><br><br><br>
## 1. 프로젝트 특징

- FastAPI로 백엔드 API 구현
- `/api/chat` 엔드포인트로 ChatGPT 응답 처리
- API 키를 프론트엔드 코드에 직접 넣지 않도록 `.env` 사용
- HTML/CSS/JavaScript 기반 floating chatbot UI 구현
- API 키가 없을 때도 화면 테스트가 가능한 데모 모드 제공
- Swagger 문서 자동 제공

## 2. 프로젝트 구조

```text
fastapi_chatgpt_chatbot_project/
├─ app/
│  ├─ main.py                         # FastAPI 실행 파일
│  ├─ schemas.py                      # 요청/응답 데이터 모델
│  ├─ services/
│  │  └─ openai_service.py            # OpenAI API 호출 서비스
│  └─ static/
│     ├─ index.html                   # 챗봇 메인 화면
│     ├─ style.css                    # 챗봇 UI 스타일
│     └─ app.js                       # 챗봇 프론트엔드 동작
├─ .env.example                       # 환경 변수 예시
├─ .gitignore                         # Git 제외 파일 목록
├─ requirements.txt                   # 설치 패키지 목록
├─ run.bat                            # Windows 실행 스크립트
└─ README.md                          # 프로젝트 설명서
```

## 3. 실행 방법

### 3-1. 프로젝트 폴더로 이동

```bash
cd fastapi_chatgpt_chatbot_project
```

### 3-2. 가상환경 생성

```bash
python -m venv .venv
```

### 3-3. 가상환경 활성화

Windows CMD:

```bash
.venv\Scripts\activate
```

PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

### 3-4. 패키지 설치

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### 3-5. 환경 변수 파일 생성

`.env.example` 파일을 복사하여 `.env` 파일을 만듭니다.

```bash
copy .env.example .env
```

`.env` 파일을 열고 OpenAI API 키를 입력합니다.

```env
OPENAI_API_KEY=sk-본인의_API_키
OPENAI_MODEL=gpt-4o-mini
```

API 키를 입력하지 않으면 데모 모드로 실행됩니다.

### 3-6. 서버 실행

```bash
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

또는 Windows에서 다음 파일을 실행합니다.

```bash
run.bat
```

## 4. 접속 주소

챗봇 화면:

```text
http://127.0.0.1:8000
```

Swagger API 문서:

```text
http://127.0.0.1:8000/docs
```

서버 상태 확인:

```text
http://127.0.0.1:8000/api/health
```

## 5. Swagger 테스트 방법

1. 브라우저에서 `http://127.0.0.1:8000/docs` 접속
2. `POST /api/chat` 클릭
3. `Try it out` 클릭
4. Request body에 아래 예시 입력

```json
{
  "message": "FastAPI가 무엇인지 설명해줘",
  "history": []
}
```

5. `Execute` 클릭
6. `reply` 값으로 챗봇 답변 확인

## 6. 중요한 보안 수정 사항

제공된 기존 React 코드에는 OpenAI API 키가 프론트엔드 JavaScript 안에 직접 작성되어 있었습니다. 프론트엔드 코드는 브라우저에서 누구나 확인할 수 있으므로 API 키를 넣으면 안 됩니다.

이 프로젝트에서는 API 키를 `.env` 파일에 저장하고, FastAPI 서버에서만 읽도록 수정했습니다. `.env` 파일은 `.gitignore`에 포함되어 GitHub에 올라가지 않도록 설정했습니다.

## 7. GitHub 업로드 명령

```bash
git init
git add .
git commit -m "Initial FastAPI ChatGPT chatbot project"
git branch -M main
git remote add origin 본인_깃허브_저장소_URL
git push -u origin main
```
