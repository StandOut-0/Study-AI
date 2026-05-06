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
print(ref.get_num() + 2)


class MyNumber1:
    def __init__(self, num):
        self.num = num

    def __len__(self):
        return self.num
    
# class MyNumber2:
#     def __init__(self, num):
#         self.num = num

ref1 = MyNumber1(100)
# ref2 = MyNumber2(100)
print(len(ref1))
# print(len(ref2))


class MyBox:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

box = MyBox([1, 2, 3])
print(len(box))   # 3
print(1 in box)   # True
print(2 in box)   # True
print(3 in box)   # True


class MyList:
    def __init__(self, data):
        self.data = data

    # def __len__(self):
    #     return len(self.data)
    
    # def __getitem__(self, index):
    #     return self.data[index]
    
    # def __str__(self):
    #     return str(self.data)
    
mylist = MyList([1, 2, 3])
print(len(mylist))   # 3
print(mylist[0])     # 1
print(mylist[1])     # 2
print(mylist[2])     # 3
print(mylist)        # [1, 2, 3]