def test_error():
    a = 1
    b = 0
    c = a / b
    print(c)

if __name__ == '__main__':
    try:
        test_error()
    except Exception as e:
        print(e)

def test_int_error():
      try:
            num = int(input("정수를 입력하세요: "))
            print(num)
      except ValueError:
            print("정수를 입력하세요.")
      except Exception as e:
            print(e)

test_int_error()


def except_pass():
    lst = ['3', '예외처리', '2', '1']
    digit_num = []
    for idx in range(len(lst)):
            try:
                digit_num.append(int(lst[idx]))
                print('try: ', digit_num)
            except ValueError:
                pass
            else:
                print('else: ', digit_num)
            finally:
                print('finally: ', digit_num)
    print(digit_num)

except_pass()

import math
def test_finally():
     try:
          radius = float(input("반지름을 입력하세요: "))
     except ValueError:
          print("반지름을 입력하세요.")
     except Exception as e:
          print(e)
     else:
         print('반지름: ', radius)
         print('원면적: ', math.pi * math.pow(radius, 2))
     finally:
          print('구문종료')
test_finally()


