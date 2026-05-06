class OOP:
    __num = 0
    def __init__(self, num):
        self.__num = num

    def __add__(self, value):
        return self.__num + value
    
    def __sub__(self, value):
        return self.__num - value

    def __mul__(self, value):
        return self.__num * value

    def __truediv__(self, value):
        return self.__num / value
    
    def get_num(self):
        return self.__num
    def set_num(self, num):
        self.__num = num

ref = OOP(100)
print(ref.get_num())