# 샘플 Python 스크립트입니다.

# Ctrl+F5을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.

import torch

def print_hi(name):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
    print(f'Hi, {name}')  # 중단점을 전환하려면 F9을(를) 누릅니다.


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    print_hi('PyCharm')


    print(torch.cuda.is_available())

    if torch.cuda.is_available():
        print(torch.cuda.get_device_name(0))
    else:
        print("CUDA GPU 없음 (CPU 사용)")

    x = torch.Tensor(3, 4)
    print(x)

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
