import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
if False:
    pass

print(len(titanic[titanic.duplicated()]))
print(titanic.duplicated().sum())

duplicated_to_first = titanic.duplicated(keep='first')
print(duplicated_to_first.sum())

duplicated_to_last = titanic.duplicated(keep='last')
print(duplicated_to_last.sum())

duplicated_all = titanic.duplicated(keep=False)
print(duplicated_all.sum())