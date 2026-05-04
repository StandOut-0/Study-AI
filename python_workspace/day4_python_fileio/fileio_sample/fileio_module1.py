
import os

def test_w(txt):
    fname = 'testa.txt'
    f=open(fname, 'w', encoding='utf-8')
    f.write(txt)
    f.close()
    print(os.getcwd(),'에 {0}가 저장되었습니다.'.format(fname))

def test_x(txt):
    fname = 'testb.txt'
    f=open('D:\\study\\sk_playdata\\study_ai\\python_workspace\\day4_python_fileio\\testb.txt', 'x', encoding='utf-8')
    f.write(txt)
    f.close()
    print(os.getcwd(),'에 {0}가 저장되었습니다.'.format(fname))

def test_a(txt):
    f=open('testc.txt', 'a',  encoding='utf-8')
    f.write(txt+'\n')
    f.close()

def test_r(r_mode):
    f=open('testc.txt', 'r',  encoding='utf-8')
    if r_mode  == 'r':
        print(f.read())
    elif r_mode == 'rl':
        while True:
            line = f.readline()
            if not line:
                break
            print(line)
            user_input = input('다음 라인을 읽으시겠습니까? (y/n)')
            if user_input == 'y':
                continue
            else:
                break

    elif r_mode == 'rls':
        print(f.readlines())
    # f.close()


def test_writelines():
    tp = ('a', 'b', 'c')
    ls = ['e', 'f', 'g']
    f = open('testa.txt', 'w', encoding='utf-8')
    f.writelines(tp)
    f.writelines('\n')
    f.writelines(ls)
    # f.writelines([str(tp)+'\n', str(ls)+'\n'])
    f.close()

def test_osmodule():
    system_user = os.getlogin() # 사용자 이름
     
     
    print(system_user+'의 현재 위치는'+os.getcwd()+'입니다.') # 현재 위치
    print(os.listdir()) # 현재 위치의 모든 파일 목록
    
    work_dir = 'D:\\study\\sk_playdata\\study_ai\\python_workspace\\day4_python_fileio\\folder'
    os.mkdir(work_dir) # 새로운 폴더 생성

    os.chdir(work_dir) # 새로운 폴더로 이동
    print(system_user+'의 현재 위치는'+os.getcwd()+'입니다.') # 현재 위치
    print(os.listdir()) # 현재 위치의 모든 파일 목록

    f = open('sample.txt', 'w', encoding='utf-8') # 새로운 파일 생성
    f.write('새로운 파일을 작성하였습니다.')
    f.close()
    print(os.getcwd()+'에 새로운 파일이 저장되었습니다.')   
