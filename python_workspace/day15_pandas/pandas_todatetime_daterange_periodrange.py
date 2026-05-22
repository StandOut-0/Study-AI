import pandas as pd

if False:
    df = pd.DataFrame({'date': ['2020-01-01', '2020-02-01', '2020-03-01']})
    print(df.info())
    df['date'] = pd.to_datetime(df['date'])
    print(df.info())


    dates = pd.date_range(start='2020-01-01', end='2020-03-01', freq='D')
    print(dates)

date_times = pd.period_range(start='2020-01-01', periods=20, freq='3h')
print(date_times)