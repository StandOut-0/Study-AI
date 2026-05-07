
def func_pass():
    print('Hello Python')
    pass

def func_noreturn():
    '나의 설명이 보이나요?'
    print('Hello Python')
    return

def func_has_var(a, b):
    print(a, b)
    return a + b

def func_several_return(a, b):
    print(a, b)
    return a + b, a - b


if __name__ == "__main__":
    help(func_noreturn)
    func_pass()
    func_noreturn()
    print(func_has_var(1, 2))
    print(func_several_return(1, 2))    