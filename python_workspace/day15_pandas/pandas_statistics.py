import numpy as np
import pandas as pd

if False:
    df = pd.DataFrame({'A': [1, None, 9], 'B': [4, 5, 6]})
    print(df)
    print(df.mean())
    print(df.mean(skipna=True))
    print(df.mean(axis=1))

    print('--'*50)
    print(df.median())
    print(df.median(skipna=False))

    print(df.min())
    print(df.max())
        
    print('--'*50)
    print(df.std())
    print(df.var())
    print(df.cov())

df = pd.DataFrame({'name': ['hong', 'kim', 'heo'],
                   'kor': [80, 90, 75],
                   'eng': [80, 95, 100],
                })
print(df)
print('--'*50)
print(df[['kor', 'eng']].corr(method='pearson'))
print('--'*50)
print(df[['kor', 'eng']].corr(method='spearman'))
print('--'*50)
print(df[['kor', 'eng']].corr(method='kendall'))