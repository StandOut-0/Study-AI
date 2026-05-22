import pandas as pd
import seaborn as sns

titan = sns.load_dataset('titanic')
if False: 
    df = titan.loc[7:16, ['survived', 'sex', 'age', 'embark_town']]
    group_res = df.groupby(['survived', 'sex'])
    print(group_res)
    print('--'*50)
    print(group_res.groups)
    print('--'*50)
    print(df.groupby('embark_town').mean(numeric_only=True))

df =  titan.loc[7:16, ['survived', 'sex', 'age', 'fare']]
def mean_min(x):
    return x.mean()- x.min()
result = df.groupby(['survived', 'sex']).agg(
        mean=('age', 'mean'),
        min=('age', 'min'),
        diff=('age', mean_min)
)
# print(result)

print('--'*50)
result = df.groupby(['survived', 'sex']).agg(
    {
        'age': ['mean', 'min', 'max'],
        'fare': ['mean', 'min', 'max']
    }
)
print(result)



