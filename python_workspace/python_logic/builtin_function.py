# 파이썬 내장함수
# https://docs.python.org/ko/3/library/functions.html

# abs() : 절대값을 반환하는 함수
print("abs(): 절대값반영 (예)", abs(-5))  # 5
# all() : 모든 요소가 참인지 확인하는 함수
print("all(): 모든 요소가 참인지 확인 (예)", all([True, True, False]))  # False
# any() : 하나라도 참인 요소가 있는지 확인하는 함수
print("any(): 하나라도 참인 요소가 있는지 확인 (예)", any([False, False, True]))  # True
# ascill() : 객체를 아스키 코드로 변환하는 함수
print("ascii(): 객체를 아스키 코드로 변환 (예)", ascii('가'))  # '\uac00'

# bin() : 정수를 이진수 문자열로 변환하는 함수
print("bin(): 정수를 이진수 문자열로 변환 (예)", bin(10))  # '0b1010'
# bool() : 객체를 불리언 값으로 변환하는 함수
print("bool(): 객체를 불리언 값으로 변환 (예)", bool(0))  # False
# byte() : 객체를 바이트 객체로 변환하는 함수
print("byte(): 객체를 바이트 객체로 변환 (예)", bytes('가', 'utf-8'))  # b'\xea\xb0\x80'

# chr() : 아스키 코드 값을 문자로 변환하는 함수
print("chr(): 아스키 코드 값을 문자로 변환 (예)", chr(97))  # 'a'

# dict() : 객체를 딕셔너리로 변환하는 함수
print("dict(): 객체를 딕셔너리로 변환 (예)", dict(a=1, b=2))  # {'a': 1, 'b': 2}
# dir() : 객체의 속성이나 메서드 목록을 반환하는 함수
# 빈 리스트를 넣으면, 파이썬은 "리스트라면 기본적으로 가지고 있는 기능(메서드)들"을 리스트 형태로 반환한다.
print("dir(): 객체의 속성이나 메서드 목록 반환 (예)", dir([]))  # 리스트의 메서드 목록
# divmod() : 두 숫자를 나눈 몫과 나머지를 튜플로 반환하는 함수
print("divmod(): 두 숫자를 나눈 몫과 나머지를 튜플로 반환 (예)", divmod(10, 3))  # (3, 1)

# enumerate() : 반복 가능한 객체를 인덱스와 함께 반환하는 함수
print("enumerate(): 반복 가능한 객체를 인덱스와 함께 반환 (예)", list(enumerate(['a', 'b', 'c'])))  # [(0, 'a'), (1, 'b'), (2, 'c')]
# eval() : 문자열로 표현된 파이썬 식을 실행하는 함수
print("eval(): 문자열로 표현된 파이썬 식을 실행 (예)", eval('1 + 2 * 3'))  # 7
# exec() : 문자열로 표현된 파이썬 코드를 실행하는 함수
code = "new_var = 10 + 20"
exec(code)
print("exec(): 문자열로 표현된 파이썬 코드를 실행 (예)", new_var)  # 30 

# filter() : 반복 가능한 객체에서 조건에 맞는 요소를 걸러내는 함수
numbers = [-2, -1, 0, 1, 2]
filtered_numbers = filter(lambda x: x > 0, numbers)
print("filter(): 반복 가능한 객체에서 조건에 맞는 요소 걸러내기 (예)", list(filtered_numbers))  # [1, 2]
# float() : 객체를 부동 소수점 숫자로 변환하는 함수
print("float(): 객체를 부동 소수점 숫자로 변환 (예)", float('3.14'))  # 3.14
# format() : 문자열을 포맷하는 함수
print("format(): 문자열 포맷 (예)", format(3.14159, '.2f'))  # '3.14'   
# frozenset() : 객체를 변경 불가능한 집합으로 변환하는 함수
soft_set = frozenset({1, 2, 3})
# soft_set.add(4)  # 에러: frozenset은 변경할 수 없음

# globals() : 현재 전역 심볼 테이블을 딕셔너리로 반환하는 함수
# 지금 내 파이썬 프로그램이 기억하고 있는 모든 변수, 함수, 임포트한 라이브러리의 목록을 딕셔너리 형태로 반환하고 .keys()를 붙이면 그 이름(변수명 등)들만 쫙 뽑아서 보여주게 된다.
print("globals(): 현재 전역 심볼 테이블 반환 (예)", globals().keys())

# hash() : 객체의 해시 값을 반환하는 함수
print("hash(): 객체의 해시 값 반환 (예)", hash('hello'))  # 해시 값은 객체의 고유한 식별자로, 동일한 객체는 동일한 해시 값을 가지며, 다른 객체는 다른 해시 값을 가집니다. 문자열 'hello'의 해시 값은 실행할 때마다 다를 수 있습니다.
# help() : 객체에 대한 도움말을 출력하는 함수
print("help(): 객체에 대한 도움말 출력 (예)", help(len))  # len
# hex() : 정수를 16진수 문자열로 변환하는 함수
print("hex(): 정수를 16진수 문자열로 변환 (예)", hex(255))  # '0xff'

# id() : 객체의 고유한 식별자를 반환하는 함수
a = 10
print("id(): 객체의 고유한 식별자 반환 (예)", id(a))  # a의 메모리 주소
# input() : 사용자로부터 입력을 받는 함수
# name = input("input(): 사용자로부터 입력 받기 (예) 이름을 입력하세요: ")  # 사용자 입력을 기다립니다.
# int() : 객체를 정수로 변환하는 함수
print("int(): 객체를 정수로 변환 (예)", int('123'))  # 123
# isinstance() : 객체가 특정 클래스의 인스턴스인지 확인하는 함수
print("isinstance(): 객체가 특정 클래스의 인스턴스인지 확인 (예)", isinstance(123, int))  # True
# issubclass() : 클래스가 다른 클래스의 서브클래스인지 확인하는 함수
print("issubclass(): 클래스가 다른 클래스의 서브클래스인지 확인 (예)", issubclass(bool, int))  # True
# iter() : 반복 가능한 객체의 반복자(iterator)를 반환하는 함수
my_iter = iter([1, 2, 3])
print("iter(): 반복 가능한 객체의 반복자 반환 (예)", next(my_iter))  # 1
print("iter(): 반복 가능한 객체의 반복자 반환 (예)", next(my_iter))  # 2
print("iter(): 반복 가능한 객체의 반복자 반환 (예)", next(my_iter))  # 3

# len() : 객체의 길이를 반환하는 함수
print("len(): 객체의 길이 반환 (예)", len("Hello, World!"))  # 13
# list() : 객체를 리스트로 변환하는 함수
print("list(): 객체를 리스트로 변환 (예)", list('abc'))  # ['a', 'b', 'c']

# map() : 반복 가능한 객체의 각 요소에 함수를 적용하는 함수
# 사용자로부터 입력받은 문자열들을 한꺼번에 숫자로 바꿀때 map을 제일 많이 사용된다.
str_list = ["1", "5", "10"]
int_list = list(map(int, str_list))
print("map(): 반복 가능한 객체의 각 요소에 함수 적용 (예)", int_list)  # [1, 5, 10]
# max() : 인자 중 최대값을 반환하는 함수
print("max(): 최대값 반환 (예)", max(5, 3, 8))  # 8 
# memoryview() : 객체의 메모리 뷰를 반환하는 함수
# bytes 객체를 메모리 뷰로 변환하여 반환합니다. 메모리 뷰는 원본 객체의 데이터를 직접 참조하므로, 메모리 효율적으로 데이터를 처리할 수 있습니다.
print("memoryview(): 객체의 메모리 뷰 반환 (예)", memoryview(b'hello'))  # <memory at 0x7f8c2b3e5c40>
# min() : 인자 중 최소값을 반환하는 함수
print("min(): 최소값 반환 (예)", min(5, 3, 8))  # 3

# next() : 반복자의 다음 요소를 반환하는 함수
my_iter = iter([1, 2, 3])
print("next(): 반복자의 다음 요소 반환 (예)", next(my_iter))  # 1
print("next(): 반복자의 다음 요소 반환 (예)", next(my_iter))  # 2
print("next(): 반복자의 다음 요소 반환 (예)", next(my_iter))  # 3

# object() : 새로운 객체를 반환하는 함수
print("object(): 새로운 객체 반환 (예)", object())  # <object object at 0x7f8c2b3e5c40>
# oct() : 정수를 8진수 문자열로 변환하는 함수
print("oct(): 정수를 8진수 문자열로 변환 (예)", oct(64))  # '0o100'
# ord() : 문자의 유니코드 코드 포인트를 반환하는 함수
print("ord(): 문자의 유니코드 코드 포인트 반환 (예)", ord('A'))  # 65

# pow() : 제곱을 계산하는 함수
print("pow(): 제곱 계산 (예)", pow(2, 3))  # 8
# print() : 객체를 문자열로 출력하는 함수
print("print(): 객체를 문자열로 출력 (예)", "Hello, World!")  # Hello, World!

# range() : 정수 시퀀스를 생성하는 함수
print("range(): 정수 시퀀스 생성 (예)", list(range(5)))  # [0, 1, 2, 3, 4]
# repr() : 객체의 공식 문자열 표현을 반환하는 함수
print("repr(): 객체의 공식 문자열 표현 반환 (예)", repr('Hello'))  # "'Hello'"
# reversed() : 시퀀스의 역순 반복자를 반환하는 함수
print("reversed(): 시퀀스의 역순 반복자 반환 (예)", list(reversed([1, 2, 3])))  # [3, 2, 1]
# round() : 숫자를 반올림하는 함수
print("round(): 숫자 반올림 (예)", round(3.14159, 2))  # 3.14

# set() : 객체를 집합으로 변환하는 함수
print("set(): 객체를 집합으로 변환 (예)", set([1, 2, 2, 3]))  # {1, 2, 3}
# slice() : 시퀀스의 슬라이스 객체를 반환하는 함수
ranking_a = ["철수", "영희", "민수", "길동"]
ranking_b = ["사과", "배", "포도", "귤"]
top_three = slice(0, 3)
print(ranking_a[top_three]) # ['철수', '영희', '민수']
print(ranking_b[top_three]) # ['사과', '배', '포도']
# sorted() : 반복 가능한 객체를 정렬하는 함수
print("sorted(): 반복 가능한 객체 정렬 (예)", sorted([3, 1, 2]))  # [1, 2, 3]
# str() : 객체를 문자열로 변환하는 함수
print("str(): 객체를 문자열로 변환 (예)", str(123))  # '123'
# sum() : 반복 가능한 객체의 합을 반환하는 함수
print("sum(): 반복 가능한 객체의 합 반환 (예)", sum([1, 2, 3]))  # 6

# tuple() : 객체를 튜플로 변환하는 함수
# tuple은 아주 쉽게 말해서 '수정할 수 없는 리스트'[]가 아닌 ()로 감싼다.
print("tuple(): 객체를 튜플로 변환 (예)", tuple([1, 2, 3]))  # (1, 2, 3)

# zip() : 여러 반복 가능한 객체를 병렬로 묶는 함수
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print("zip(): 여러 반복 가능한 객체 병렬로 묶기 (예)", list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# import() : 모듈을 동적으로 임포트하는 함수
# importlib 모듈의 import_module 함수를 사용하여 모듈을 동적으로 임포트할 수 있습니다.
import importlib

imgotodelete = "Bye"
print(imgotodelete)  # Bye
del imgotodelete
print(imgotodelete)  # NameError: name 'imgotodelete' is not defined