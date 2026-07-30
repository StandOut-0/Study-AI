#!/usr/bin/env bash

# 오류가 발생하면 이후 명령을 실행하지 않고 즉시 종료합니다.
set -e

# 학습 데이터를 생성합니다.
python 01_create_dataset.py

# 4bit QLoRA 기반 SFT 학습을 실행합니다.
python 02_train_sft.py

# 학습 완료 메시지를 출력합니다.
echo "학습이 완료되었습니다. 대화형 추론은 python 03_inference.py 로 실행하세요."
