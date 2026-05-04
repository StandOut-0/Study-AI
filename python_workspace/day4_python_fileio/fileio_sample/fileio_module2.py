import os
import pickle

def test_binary():
    data = {1:'Hi', 2:'Im', 3:'Sanghee'}
    f = open('testbinary.dat', 'wb')
    pickle.dump(data, f)

    f = open('testbinary.dat', 'rb')
    data = pickle.load(f)
    print(data)
    f.close()

def test_filexists(file, new_name):
    # 1. 파일명을 절대 경로로 변환
    filepath = os.path.abspath(file) 
    
    # 2. 존재 여부 확인 (인자는 하나만!)
    if os.path.exists(filepath):
        print(f"파일 존재 확인: {os.path.exists(filepath)}")

        filename = os.path.basename(filepath)
        print(f"파일명만: {filename}")
        print(f"드라이브: {os.path.splitdrive(filepath)[0]}")
        print(f"확장자 제외 이름: {os.path.splitext(filename)[0]}")
        print(f"확장자: {os.path.splitext(filename)[1]}")
        print(f"폴더 위치: {os.path.dirname(filepath)}")
        print(f"분리 결과(폴더, 파일): {os.path.split(filepath)}")
        
        target_path = os.path.join(os.path.dirname(filepath), new_name)
        
        os.rename(filepath, target_path)
        print(f'\n이름 변경 완료 -> {new_name} 존재 여부: {os.path.exists(target_path)}')
    else:
        print(f"'{file}' 파일이 없습니다. 경로를 확인해주세요!")
