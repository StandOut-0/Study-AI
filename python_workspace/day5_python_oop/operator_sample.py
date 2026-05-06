def func_bool():
    flag = True
    a = 1 
    b = 2
    print(flag, type(flag), bool(flag))

    print(
        bool({1, 2, 3}),
        bool(-1), 
        bool('0'), 
        bool(1 == 1), 
        bool(a > 0 and b > 0))
    print(
        bool(0), 
        bool(""), 
        bool({}), 
        bool(1 == -1))

if __name__ == "__main__":
    func_bool()