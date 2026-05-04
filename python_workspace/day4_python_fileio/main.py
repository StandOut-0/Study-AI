import fileio_sample.fileio_module1 as fs
import while_sample.while_sample as ws  

prompt = """
              1. 파일 입출력 테스트 - w
              2. 파일 입출력 테스트 - writelines
              3. 파일 입출력 테스트 - x
              4. 파일 입출력 테스트 - a
              5. 파일 입출력 테스트 - r
              6. while문 예시
              7. 유니코드 변환기
              8. os모듈 예시
              9. 메뉴 출력
              10. 프로그램 종료"""

def menu():
    print(prompt)
    while True:
        try:
            no = int(input('메뉴 번호 입력 : '))
            if no == 1:
                txt = str(input('파일에 저장할 내용 입력 : '))
                fs.test_w(txt)
            elif no == 2:
                fs.test_writelines()
            elif no == 3:
                txt = str(input('파일에 저장할 내용 입력 : '))
                fs.test_x(txt)
            elif no == 4:
                txt = str(input('파일에 저장할 내용 입력 : '))
                fs.test_a(txt)
            elif no == 5:
                r_mode = str(input('읽기모드입력 (r, rl, rls) : '))
                fs.test_r(r_mode)
            elif no == 6:
                ws.test_while()
            elif no == 7:
                ws.turntounicode()
            elif no == 8:
                fs.test_osmodule()
            elif no == 9:
                print(prompt)
            elif no == 10:
                print('프로그램 종료')
                break
        except Exception as e:
            print(e)

if __name__ == '__main__':
    menu()
    