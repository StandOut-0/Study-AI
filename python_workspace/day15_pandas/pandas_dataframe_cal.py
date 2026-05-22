import pandas as pd
import seaborn as sns

titan = sns.load_dataset('titanic')
df = titan.loc[10:16, ['age']]
print(df)
print('--'*50)
print(df/2)