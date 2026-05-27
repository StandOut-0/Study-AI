import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import joblib

iris = load_iris()

X = iris.data
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y
df['target_names'] = iris.target_names[iris.target]

if False:

    print('head()-----------------------------------------')
    print(df.head())

    print('shape-----------------------------------------')
    print('데이터크기', df.shape)

    print('info()-----------------------------------------')
    print(df.info())

    print('value_counts()-----------------------------------------')
    print(df['target_names'].value_counts())





    plt.rcParams['font.family'] = 'Malgun Gothic'  # 맑은 고딕
    plt.rcParams['axes.unicode_minus'] = False

    sns.countplot(data=df, x='target_names')
    plt.title('iris 품종별 데이터 개수')
    plt.xlabel('품종')
    plt.ylabel('개수')
    plt.show()

    sns.pairplot(df, hue='target_names')
    plt.show()




X = df[feature_names]
Y = df['target']
if False:
    print('입력데이터 크기 확인하기-----------------------------------------')
    print('입력데이터 x크기: ', X.shape)
    print('정답데이터 x크기: ', Y.shape)


X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y)
if False:
    print('학습/테스트용 데이터 확인하기-----------------------------------------')
    print(X_train.shape)
    print(X_test.shape)
    print(y_train.shape)
    print(y_test.shape)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

if False:
    print('데이터 전처리 - 표준화-----------------------------------------')
    print(X_train.head())
    print(X_train_scaled[:5])


print('model-----------------------------------------')
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
print(y_pred)
print(y_test.values)

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)



if False:
    print('model 평가-----------------------------------------')
    print(classification_report(y_test, y_pred, target_names=target_names))

    print(confusion_matrix(y_test, y_pred))
    sns.heatmap(confusion_matrix(y_test, y_pred),annot=True,fmt='g', cmap='Blues',
                xticklabels=target_names, yticklabels=target_names)
    plt.show()


if False:
    print('새로운 데이터로 예측 결과 확인-----------------------------------------')
    new_data = [[5.1, 3.5, 1.4, 0.2]]
    new_data_scaled = scaler.transform(new_data)
    new_pred = model.predict(new_data_scaled)
    pred_name = target_names[new_pred[0]]


    print(pred_name)


print('모델 저장-----------------------------------------')
joblib.dump(model, 'iris_random_forest_model.pkl')
joblib.dump(scaler, 'iris_random_forest_scaler.pkl')


print('모델 불러오기-----------------------------------------')
loaded_model = joblib.load('iris_random_forest_model.pkl')
loaded_scaler = joblib.load('iris_random_forest_scaler.pkl')

sample = [[6.2, 3.5, 5.4, 2.3]]
sample_scaled = loaded_scaler.transform(sample)
sample_pred = loaded_model.predict(sample_scaled)
pred_name = target_names[sample_pred[0]]
print(sample_pred, pred_name)