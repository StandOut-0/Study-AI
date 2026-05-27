

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from numpy import dtype
from sklearn.datasets import load_wine, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import TensorDataset, DataLoader

from teacher.ML_sample_torch import train_dataset

# 실습 test_wine 1~6번 까지를 다음 데이터셋을 사용해 torch로 구현하라




# sklearn.datasets의 load_wine()을 사용하여 데이터를 불러오시오
# breast cancer 데이터셋
# wine = load_wine()
caner = load_breast_cancer()
df = pd.DataFrame(caner.data, columns=caner.feature_names)
df['target'] = caner.target

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
    sns.countplot(data=df, x='target', hue='target')
    plt.show()

    sns.pairplot(data=df, hue='target')
    plt.show()






# 입력데이터 x와 정답데이터 y를 분리하시오.
# x = caner.data
x = pd.DataFrame(caner.data, columns=caner.feature_names)
y = df['target']
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
if False:
    print("전처리 - 학습용 데이터", '-' * 30)
    print(x_train.head())
    print(x_train_scaled[:5])


# 입력데이터 float32로 변환, 정답데이터는 croeeentropyloss사용을 위해 long타입으로 변환
import torch
x_train_tensor = torch.tensor(x_train_scaled, dtype=torch.float32)
x_test_tensor = torch.tensor(x_test_scaled, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
y_test_tensor = torch.tensor(y_test.values, dtype=torch.long)
if False:
    print(x_train_tensor[:5], x_test_tensor[:5],
      y_train_tensor[:5], y_test_tensor[:5])

# tensordataset은 입력데이터와 정답데이터를 하나로 묶어 batch 단위로 나누어 학습에 사용한다.
train_dataset = TensorDataset(x_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)


# PyTorch 신경망 모델 정의
from torch.nn.modules import *
class canerNet(nn.Module):
    pass


..? 엥 정답주셧는데 내가 어디까지간거지 훔.. 정지



