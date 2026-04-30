# 주석

"""
여러줄 주석
"""

num = 1 + 2
print('num 변수가 가진 값은:', num)

x, y, z = 10, 20, 30
print('x 변수가 가진 값은:', x)
print('y 변수가 가진 값은:', y)
print('z 변수가 가진 값은:', z)
k = m = n = z = 100
print(x, y, z, sep=', ')
print(k, m, n, sep=', ')

first, second = 123, 456
print('first:', first, 'second:', second)
first, second = second, first
print('first:', first, 'second:', second)

value = 10
for i in range(5):
    value += 10
    print('value:', value)
value *= 2
print('최종 value:', value)
# value /= 2
value //= 2
print('최종 value:', value)
value **= 2
print('최종 value:', value)

print("그냥작성하고 줄바꿈을 하고싶을땐 이렇게\n작성하면 됩니다.")
