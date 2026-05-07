def tmax(a, b= 100):
    print(f'a: {a}, b: {b}, type: {type(a)}, type: {type(b)}')
    result = 0
    if a > b:
        result = a
    else:
        result = b
    return "id값이 같은가? ",id(result)
    
# print(tmax(1, 2))
tmax(2)

def func_callby_value():
    'tmax() 함수 테스트용'
    result = tmax(30, 20)
    "id값이 같은가? ",id(result)
    # result = tmax(10)
    # result = tmax(10, 20, 30, 40)
    print(result)

func_callby_value()

def list_in_max(alist):
    print(f'alist: {alist}, 주소: {id(alist)}')
    
    max = alist[0]
    for i in range(1, len(alist)):
        if alist[i] > max:
            max = alist[i]
    return max

alist = [1, 2, 3, 4, 5]
print(list_in_max(alist))


def func_callby_ref():
    'list_in_max() 함수 테스트용'
    alist = [1, 2, 3, 4, 5]
    print(list_in_max(alist))
    print(id(alist))


