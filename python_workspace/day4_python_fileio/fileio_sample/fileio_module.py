import os

def test_fwrite():
    f=open('testa.txt', 'w', encoding='utf-8')
    f.write(
"""hello world 안녕 ?! ★
줄바꿈 테스트입니다.
""")
    f.write(
'\n혹은 이렇게 줄바꿈 하던가\n줄바꿈 테스트입니다.')