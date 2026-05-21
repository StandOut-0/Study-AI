import numpy as np
import pandas as pd

s = pd.Series([12356784, 5437689, 3440451, 2805246], index=['서울', '부산', '인천', '대구'])
if False : 
    rint('pd.Series-------------------------')
    print(s)
    print('index-------------------------')
    print(s.index)
    print('values-------------------------')
    print(s.values)

    print(s)
    print('name-------------------------')
    s.name = '인구'
    s.index.name = '지역'
    print(s)

    print(s/1000)

    print(s.iloc[1])
    print(s['부산'])
    print(s.loc['부산'])
    print(s.부산)


    print(s.iloc[[0, 3, 1]])
    print(s.loc[['서울', '대구', '인천']])

    print(s[(300e4 < s) & (s < 400e4)])

    print(s[1:3])

    print('서울'in s)
    print('서울'in s.index)
    print('서울'in s.values)

for k, v in s.items():
    print(k, v)
    print('%s안에는 %s명이 있습니다.' % (k, v))