# 인덱싱
ss = 'Hi,-Python'
print(ss[0])
print(ss[4])
print(ss[-1])

# 슬라이싱 n:n:m m는 간격으로 기본값 1
print(ss[0:3]) # 0, 1, 2: Hi,
print(ss[0:5:2]) # 0, 2, 4: H,P
print(ss[::2]) # 0, 2, 4, 6: H,Pto
print(ss[::-1]) # -1, -2, -3, ... : nohtyP-iH

n1 = '1234567890'
n2 = 'abcdefghij'
n3 = n1[0:3] + n2[1:]
print(n3) # 123bcdefghij
print(n2.upper()) # ABCDEFGHIJ
print(n2.upper().lower()) # abcdefghij

"""
파이썬의 Immutable
int, float (숫자)
str (문자열)
tuple (튜플)
frozenset (얼린 집합)
bool (True/False)
"""
# n2[1]= 'B' # 에러: 문자열은 변경할 수 없음

tt2 = "ORANGE"
print(tt2.lower()) # orange
print(tt2) # ORANGE: 원본은 변경되지 않음
print(id(tt2)) # ORANGE의 메모리 주소
tt2 = "RED"
print(id(tt2)) # RED의 메모리 주소: ORANGE와 다름



# capitalize() : 문자열의 첫 글자를 대문자로, 나머지는 소문자로 변환하는 메서드
print(tt2.capitalize()) # Orange

# swapcase() : 대문자는 소문자로, 소문자는 대문자로 변환하는 메서드
print(tt2.swapcase()) # oRaNGe

# strip(), lstrip(), rstrip() : 문자열의 양쪽, 왼쪽, 오른쪽에서 공백을 제거하는 메서드
s = "   Hello, World!   "
print("start", s.strip(), "end") # "Hello, World!"
print("start", s.lstrip(), "end") # "Hello, World!   " 
print("start", s.rstrip(), "end") # "   Hello, World!"

print('|', s, '|') # |    Hello, World!   |: 공백이 포함된 원본 문자열이 출력됨
print('|', s, '|', sep='') # |    Hello, World!   | : sep=''로 설정하여 구분자 없이 출력됨

# split() : 문자열을 공백을 기준으로 나누어 리스트로 반환하는 메서드
s2 = "Python is great"
print(s2.split()) # ['Python', 'is', 'great']

# splitlines() : 문자열을 줄바꿈을 기준으로 나누어 리스트로 반환하는 메서드
s3 = "Line 1\nLine 2\nLine 3"
print(s3.splitlines()) # ['Line 1', 'Line 2', 'Line 3']

# index() : 문자열에서 특정 문자의 인덱스를 반환하는 메서드
print(s2.index('is')) # 7: 'is'가 시작하는 인덱스 위치
# print(s2.index('brrrrrr'))

# find() : 문자열에서 특정 문자의 인덱스를 반환하는 메서드 (찾지 못하면 -1 반환)
print(s2.find('is')) # 7: 'is'가 시작하는 인덱스 위치
print(s2.find('brrrrrr'))

print(len(dir(str)))    
print(dir(str))    
