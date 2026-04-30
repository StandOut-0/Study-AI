'''
신상 정보를 입력받아, 각 변수에 저장하시오. 변수명은 임의대로 지정함
이름(str), 나이(int), 성별(str, 남|여 로 입력), 키(float), 몸무게(float)
각 변수의 값을 아래의 형식으로 출력하는 코드를 작성하시오. 3가지 방식 모두 사용해 봄
홍길동은 27세 남자이고, 키는 178.5cm 몸무게는 72.0kg 입니다.
'''

name = input('이름을 입력하세요: ')
age = int(input('나이를 입력하세요: '))
gender = input('성별을 입력하세요 (남/여): ')
height = float(input('키를 입력하세요 (cm): '))
weight = float(input('몸무게를 입력하세요 (kg): '))

print(name, '은', age, '세', gender, '이고, 키는', height, 'cm 몸무게는', weight, 'kg 입니다.')
print(f'{name}은 {age}세 {gender}이고, 키는 {height}cm 몸무게는 {weight}kg 입니다.')
print('{}은 {}세 {}이고, 키는 {}cm 몸무게는 {}kg 입니다.'.format(name, age, gender, height, weight))