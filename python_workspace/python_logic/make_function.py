def hello(name):
    print(f"Hello, {name}!")
    return 

def check_type(value):
    print(f"Value: {value}, Type: {type(value)}")
    return

if __name__ == "__main__":
    print("프로그램 시작")
    hello("Alice")
    hello("Bob")
    check_type("Hello")
    check_type(123)
    check_type([1, 2, 3])
    print("프로그램 종료")
