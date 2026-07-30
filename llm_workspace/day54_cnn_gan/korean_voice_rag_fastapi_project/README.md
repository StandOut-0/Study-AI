# 한국어 음성 RAG FastAPI 프로젝트

처리 흐름: 브라우저 마이크 녹음 → Faster-Whisper 한국어 STT → SentenceTransformer 문서 검색 → 파인튜닝 모델 답변 → Edge TTS/pyttsx3 → 브라우저 스피커 재생

## 실행
```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
copy .env.example .env
python run.py
```
브라우저: `http://127.0.0.1:8000`

## 모델 적용
- 전체 모델: `models/finetuned_model` 안에 config.json, model.safetensors, tokenizer 파일 배치
- PEFT LoRA: adapter_config.json, adapter_model.safetensors 배치 후 `.env`의 BASE_MODEL_NAME을 학습 원본과 동일하게 설정
- 모델이 없을 때는 `ALLOW_DEMO_FALLBACK=true`로 STT/RAG/TTS 연결을 먼저 점검 가능

## LoRA 학습
```powershell
pip install -r requirements-training.txt
python training/train_sft.py
```
샘플 데이터 1건은 구조 확인용이므로 실제 운영 데이터로 교체해야 합니다.

## RAG 문서
`data/documents`에 UTF-8 TXT/MD 파일을 추가한 뒤 `POST /api/rag/rebuild`를 호출합니다.

## 권장 환경
- Python 3.11
- CPU: WHISPER_COMPUTE_TYPE=int8, 1.5B LLM은 느릴 수 있음
- NVIDIA GPU: LLM_DEVICE=cuda, WHISPER_DEVICE=cuda, WHISPER_COMPUTE_TYPE=float16
- Edge TTS는 인터넷 필요. 실패 시 Windows 한국어 음성 팩 기반 pyttsx3로 대체 시도

## 한글 인코딩
모든 Python/HTML/JSONL/문서는 UTF-8이며 HTML에 `<meta charset="UTF-8">`가 포함되어 있습니다.

