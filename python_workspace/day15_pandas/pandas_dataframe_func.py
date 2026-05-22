import numpy as np
import pandas as pd

if False:
    pass

data = {
 "2019": [9904312, 3448737, 2890451, 2466052],
 "2020": [9631482, 3393191, 2632035, 2431774],
 "2021": [9762546, 3512547, 2517680, 2456016],
 "2022": [9853972, 3655437, 2466338, 2473990],
 "지역": ["수도권", "경상권", "수도권", "경상권"],
 "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
} # dict 사전자료형

index_label = ['수도권', '경상권', '수도권', '경상권']
df=pd.DataFrame(data, index=index_label)
print(df)

df.loc['상이권'] = [9049404, 3448737, 2890451, 2466052, '상이권', 0.777]
print(df)
df_drop = df.drop('상이권')
print(df_drop)

df['상이메모'] = [0.777, 0.888, 0.999, 0.111, 0.111]
print(df)
df_drop= df.drop('상이메모', axis=1)
print(df_drop)

print(df)
df = df.reset_index(drop=True)
df.index = ['오상권', '일도권', '이상권', '삼이권', '사도권']
df_new = df.reindex(['일도권', '이상권', '삼이권', '사도권', '오상권'])
print(df_new)

df_new = df[['2022', '2021', '2020', '2019', '2010-2015 증가율', '지역', '상이메모']]
print(df_new)

df_new = df.transpose()
print(df_new)