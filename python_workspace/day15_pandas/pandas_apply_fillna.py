import seaborn as sns


titanic = sns.load_dataset('titanic')
if False:    
    def minus(data1, data2):
        return data1 - data2

    df = titanic.loc[:, ['survived', 'sex', 'age', 'fare']]
    print(df)

    print('--'*50)
    print(df['fare'].apply(minus, data2=10))
    print(df['fare'].apply(lambda x:minus(x, 10)))

    df = titanic.loc[:, ['age', 'fare']]
    # print(df.map('minus', data2=10))

    print('--'*50)
    print(df)
    print(df.apply('mean', axis=0))
    print(df.apply('mean', axis=1))

    def val_isnull(data):
        return data.isnull().sum()

    df = titanic.loc[:, ['age', 'fare']]
    print(df
        .pipe(lambda x: x -10)
        .pipe(val_isnull)
        .pipe(lambda x: x.sum())
        )
    

    df = sns.load_dataset('titanic')
    print(df.info())

    print(df.value_counts())
    print('--'*50)
    print(df.value_counts(
        normalize=True,
        sort=False,
        ascending=False,
        dropna=True,
    ))



    print(titanic['age'].value_counts(dropna=False))


    print(titanic.value_counts())
    print(titanic.apply(lambda x: x.value_counts(), axis=0).fillna(0.0).astype(float))


    age_mean = titanic['age'].mean()
    print(titanic['age'].isnull().sum(), titanic['age'].mean())
    titanic['age'] = titanic['age'].fillna(age_mean)
    print(titanic['age'].isnull().sum(), titanic['age'].mean())


    print(titanic['embark_town'].isnull().sum())
    # titanic['embark_town'] = titanic['embark_town'].fillna(method='bfill')
    # titanic['embark_town'] = titanic['embark_town'].bfill()

    # titanic['embark_town'] = titanic['embark_town'].fillna(method='ffill')
    titanic['embark_town'] = titanic['embark_town'].ffill()
    print(titanic['embark_town'].isnull().sum())