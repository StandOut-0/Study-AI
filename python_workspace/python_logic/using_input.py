num = input('숫자를 입력하세요: ')
print('num:', num, 'type(num):', type(num))

inum = int(num)
print('inum:', inum + 100, 'type(inum):', type(inum))

first = int(input('첫 번째 숫자를 입력하세요: '))
second = int(input('두 번째 숫자를 입력하세요: '))
print('first + second:', first + second)

# f'str': 문자열 안에 {}로 감싸서 변수나 표현식을 넣을 수 있다.
print(f'{first} + {second} = {first + second}')

# format() 메서드와 인덱스 사용
print('result1 = {} - {} = {}'.format(first, second, first - second))
print('result2 = {1} - {2} = {0}'.format(first, second, first - second))

# 소숫점 아래 자릿수 지정
print('result/ = {} / {} = {:.10000f}'.format(first, second, first / second))
print('result% = {} % {} = {}'.format(first, second, first % second))