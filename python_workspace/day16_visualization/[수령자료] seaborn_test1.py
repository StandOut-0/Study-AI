import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

def test1():
    sns.relplot(x='total_bill', y='tip', data=tips)
    plt.show( )

def test2():
    sns.relplot(x='total_bill', y='tip',  kind='line', data=tips)
    plt.show( )

def test3():
    sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips)
    plt.show( )

def test4():
    sns.pairplot(data=tips)
    # 대각선은 histogram, 그 외에는 scatter
    plt.show( )

def test5():
    sns.pairplot(tips, vars=['total_bill', 'tip', 'size', 'day'])
    plt.show( )

def test6():
    sns.pairplot(tips, y_vars=['total_bill', 'tip', 'day'], x_vars=['total_bill', 'tip'])
    plt.show( )

def test7():
    sns.pairplot(tips, vars=['total_bill', 'tip', 'size', 'day'], kind='scatter', 
        diag_kind='hist',
        hue='smoker',
        palette='pastel')
    plt.show( )

def test8():
    sns.pairplot(tips, kind='kde', diag_kind='hist', hue='smoker')
    plt.show( )

def test9():
    pivot_table = tips.pivot_table(values='tip', index='day', columns='time', 
                                   aggfunc='mean')
    sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', linewidths=0.5)
    plt.show( )

def test10():
    selected_columns = tips[['total_bill', 'tip']]
    corr = selected_columns.corr( )
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.show( )


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()