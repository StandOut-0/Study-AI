class PClass:
    __num = 10 # 정적 변수
    
    def __init__(self): # 생성자
        self.__num = 0

    def __init__(self, num): # 생성자
        self.__num = num # 오버라이딩

    def set_num(self, num):
        self.__num = num

    def get_num(self):
        return self.__num
    
pref = PClass(2)
print(pref.get_num())

class Var:
    __number = 100
    def __init__(self, num):
        self.__number = num

    def __del__(self):
        print("인스턴스 제거시 자동 호출됨", id(self))

    def get_number(self):
        return self.__number
    
    def set_number(self, num):
        self.__number = num

v1 = Var(100)
print('v1',v1.get_number(), id(v1))
v2 = Var(200)
print('v2',v2.get_number(), id(v2))
# del v1
print("--- 프로그램의 모든 코드가 종료되었습니다 ---")


print('v1 값변경:',v1.get_number(), id(v1))
v1.set_number(300)
print('v1 값변경:',v1.get_number(), id(v1))


class C:
    def ham(self, x, y):
        print('instance method ham', x, y, id(C), id(self))
class D:
    @staticmethod
    def spam(x, y):
        print('static method spam', x, y, id(D))

c = C()
d = D()
c.ham(1, 2)
d.spam(3, 4)