def test_while():
    i=0
    while i<3:
        print(i)
        i+=1
    while True:
        print(i,'번째 무한루프')
        i+=1

        if i>3:
            break

def turntounicode():
    while True:
        ch = input("문자 하나 입력 (종료는 0): ")
        
        if ch == '0': # 종료 조건
            print("변환기를 종료합니다.")
            break
            
        if len(ch) > 1:
            print("한 글자만 입력해주세요.")
            continue
            
        print(f"'{ch}'의 유니코드 값은 {ord(ch)}입니다.")