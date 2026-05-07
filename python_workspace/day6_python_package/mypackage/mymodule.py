pi = 3.141592653589793
count = 10

def sum(a, b):
    return a + b

def div(a, b):
    return a / b

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def mod(a, b):
    if b == 0:
        raise Exception("b can not be zero")
    return a % b

def max(*args):
    try:
        max_value = args[0]
        for i in range(1, len(args)):
            if args[i] > max_value:
                max_value = args[i]
        return max_value
    except:
        return None
    
def min(*args):
    try:
        min_value = args[0]
        for i in range(1, len(args)):
            if args[i] < min_value:
                min_value = args[i]
        return min_value
    except:
        return None
    
def strlen(s):
    if s is None:
        return 0
    return len(s)

if __name__ == "__main__":
    # print(max(1, 2, 3, 4, 5))
    print(strlen("helloSanghee"))
    print(strlen(""))