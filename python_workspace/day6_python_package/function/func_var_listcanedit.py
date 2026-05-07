
imglobal = 10

def func1():
    num = 10
    print(num, imglobal)


def func2():
    # print(num)
    pass

# print(num)




def func_list(plist):
    print('before:', plist, id(plist))
    plist[1] = 100
    print('after:', plist, id(plist))


def func_basic(a):
    print('before:', a, id(a)) 
    a = 100
    print('after:', a, id(a))


if __name__ == "__main__":
    func1()
    func2()
    func_list([0, 1, 2, 3, 4, 5])
    func_basic(10)


