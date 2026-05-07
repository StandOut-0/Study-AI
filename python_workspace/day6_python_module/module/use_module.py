import keyword
import os
# print(keyword.kwlist)
# print(keyword.__file__ )

# help('modules')
# help('random')

import time
print(os.getcwd())
print('localtime: ',time.localtime())
time.sleep(1)
print('localtime: ',time.localtime())

import random
print(random.random())
print(random.randint(1, 10))
print(random.randrange(1, 10, 2))


import math
print('원주율: ', math.pi)
print('5!:', math.factorial(5))

import calendar
calendar.prmonth(2022, 1)
print(__name__)

import mymodule as my
print('mymodule 더하기', my.sum(1, 2))
print(__name__)

