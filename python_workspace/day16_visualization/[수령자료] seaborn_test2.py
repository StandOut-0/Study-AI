import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

flights = sns.load_dataset('flights')

def test1():
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='year', y='passengers', data=flights)
                 
    plt.title('Number of Passengers Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Passengers')
    plt.show( )

def test2():

    flights['year'] = flights['year'].astype(str)
    flights['month'] = flights['month'].astype(str)

    flights['date'] = pd.to_datetime(
        flights['year'] + '-' + flights['month']
    )

    sorted_flights = flights.sort_values('date')

    plt.figure(figsize=(12, 6))

    sns.lineplot(
        x='date',
        y='passengers',
        data=sorted_flights
    )

    plt.title('Monthly Number of Passengers Over Time')

    plt.xlabel('Date')
    plt.ylabel('Number of Passengers')

    plt.show()

def test3():

    flights_grouped = flights.groupby(
        ['year', 'month']
    )['passengers'].sum().unstack(level=0)

    plt.figure(figsize=(12, 8))

    sns.heatmap(
        flights_grouped,
        annot=True,
        fmt="d",
        cmap="YlGnBu",
        linewidths=0.5
    )

    plt.show()

if __name__ == '__main__':
    test1()
    test2()
    test3()