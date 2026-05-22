import pandas as pd
import seaborn as sns


titanic = sns.load_dataset('titanic')
if False:
    pass


df = titanic.loc[:, ['survived', 'sex', 'age', 'embark_town']]
print(df)
print('--'*50)
print(pd.cut(df['age'], bins=3, labels=['low', 'medium', 'high']))
print('--'*50)
print(pd.qcut(df['age'], 3, labels=['low', 'medium', 'high']))


print('categories: ','--'*50)
result = pd.cut(df['age'], bins=3, labels=['low', 'medium', 'high'])
print(result.cat.categories)
print('codes: ','--'*50)
print(result.cat.codes)
