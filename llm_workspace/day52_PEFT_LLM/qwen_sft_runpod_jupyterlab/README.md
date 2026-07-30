# RunPod JupyterLab Qwen2.5 SFT 프로젝트

## 포함 파일

```text
qwen_sft_runpod_jupyterlab/
├── Qwen2.5_SFT_RunPod_JupyterLab.ipynb
├── data/
│   ├── train.jsonl
│   └── valid.jsonl
├── outputs/
│   ├── checkpoints/
│   └── qwen2.5-korean-sft-lora/
├── .env.example
├── requirements.txt
└── README.md
```

## RunPod 사용 순서

1. GPU Pod를 생성합니다.
2. JupyterLab에 접속합니다.
3. ZIP 파일을 `/workspace`에 업로드합니다.
4. JupyterLab Terminal을 엽니다.
5. 아래 명령을 실행합니다.

```bash
cd /workspace
unzip qwen_sft_runpod_jupyterlab.zip
cd qwen_sft_runpod_jupyterlab
```

6. `Qwen2.5_SFT_RunPod_JupyterLab.ipynb`를 엽니다.
7. 셀을 위에서 아래로 순서대로 실행합니다.
8. 패키지 설치 후 Import 오류가 나면 Kernel을 재시작합니다.
9. 학습 결과는 `/workspace/qwen_sft_runpod_jupyterlab/outputs`에 저장됩니다.
10. Pod 종료 전 결과 ZIP을 로컬 또는 외부 저장소로 백업합니다.

## 권장 환경

- NVIDIA GPU
- VRAM 8GB 이상
- Python 3.10 또는 3.11
- CUDA 지원 PyTorch
- `/workspace` 영구 볼륨 사용 권장

## 실행 성공 기준

- CUDA GPU 인식
- 데이터 생성 및 검증
- Tokenizer와 기본 모델 다운로드
- 4bit 양자화 모델 로드
- LoRA 학습 가능 파라미터 출력
- Training Loss 및 Evaluation Loss 출력
- `adapter_model.safetensors` 저장
- Adapter 재로드 후 한국어 답변 생성