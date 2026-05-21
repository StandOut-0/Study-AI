import numpy as np
import pandas as pd


if False:
    s = pd.Series([12356784, 5437689, 3440451, 2805246], index=['서울', '부산', '인천', '대구'])
    print(s)

    print(pd.Series(range(10)))


    data = {
        '2022': [12350000, 5430000, 3440000, 2800000],
        '2023': [12351000, 5431000, 3441000, 2810000],
        '2024': [12352000, 5432000, 3442000, 2820000],
        '2025': [12353000, 5433000, 3443000, 2830000],
        '지역': ['서울', '부산', '인천', '대구'],
        '2015~2019 증가율': [0.0283, 0.0163, 0.0982, 0.0141]
    }
    print(pd.DataFrame(data))

    columns = ['지역', '2022', '2023', '2024', '2025', '2015~2019 증가율']
    index = ['서울', '부산', '인천', '대구']
    df = pd.DataFrame(data, columns=columns, index=index)
    print(df)

    df = pd.DataFrame(data, index=index)
    print(df)

    df = pd.DataFrame(np.arange(12).reshape(3,4))
    print(df)

if False: df.to_csv('test.csv')

df4 = pd.read_csv('test.csv')
print(df4)

df4 = pd.read_csv('test.csv', index_col=0)
print(df4)