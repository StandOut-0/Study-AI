import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# sklearn.datasets의 load_wine()을 사용하여 데이터를 불러오시오
wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target
df['target_names'] = df['target'].map(
    dict(zip(range(len(wine.target_names)), wine.target_names))
)


if False:
    print(df.head())
    print(df['target_names'])





# wine의 데이터셋의 크기, 기초 통계량, 클래스별 개수를 확인하시오
if False:
    print("데이터셋의 크기", '-'*30)
    print(df.shape)
    print("기초 통계량", '-'*30)
    print(df.describe())
    print("클래스별 개수", '-'*30)
    print(df['target'].value_counts())





# wine 클래스별 데이터 개수를 그래프로 출력하시오.
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

if False:
    sns.countplot(data=df, x='target_names', hue='target')
    plt.show()

    sns.pairplot(data=df, hue='target_names')
    plt.show()






# 입력데이터 x와 정답데이터 y를 분리하시오.
x = df.drop(columns=['target', 'target_names'])
y = df['target_names']
if False:
    print("입력데이터 x", '-' * 30)
    print(x.shape)
    print(x.head())
    print("정답데이터 y", '-' * 30)
    print(y.shape)
    print(y.head())





# 전체 데이터중 80%는 학습용, 20%는 테스트용으로 분리하시오
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)
if False:
    print("학습용 데이터", '-' * 30)
    print(x_train.head())
    print(y_train.head())
    print("테스트용 데이터", '-' * 30)
    print(x_test.head())
    print(y_test.head())






# standardscaler를 사용해 실습데이터와 테스트 데이터를 표준화하시오
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
print("전처리 - 학습용 데이터", '-' * 30)
print(x_train.head())
print(x_train_scaled[:5])





