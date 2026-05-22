import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
if False:
    pass


print(titanic.isnull().sum())   
delete_age_deck = titanic.dropna(subset=['age', 'deck'])
print(delete_age_deck.isnull().sum())   

delete_all_null = delete_age_deck.dropna()
print(delete_all_null.isnull().sum())