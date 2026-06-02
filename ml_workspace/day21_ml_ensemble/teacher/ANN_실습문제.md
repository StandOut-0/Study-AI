# ANN(Artificial Neural Network) 실습문제

# 심화 실습문제

## 실습문제 1. 상관계수(Correlation Coefficient) 분석

1. 상관계수(Correlation Coefficient)의 의미를 설명하시오.
2. 상관계수 값의 범위를 작성하시오.
3. 상관계수가 0.95인 경우 모델 성능을 평가하시오.
4. 상관계수와 MSE의 차이점을 설명하시오.

---

## 실습문제 2. 과적합(Overfitting) 분석

1. 과적합(Overfitting)의 의미를 설명하시오.
2. 은닉노드를 50개 이상으로 증가시켰을 때 발생할 수 있는 문제를 설명하시오.
3. 과적합을 방지하는 방법을 3가지 이상 작성하시오.

---

## 실습문제 3. 하이퍼파라미터 튜닝

다음 항목을 변경하여 실험을 수행하시오.

* Epoch
* Learning Rate
* Hidden Node 수
* Hidden Layer 수
* Activation Function

### 작성 내용

| 실험번호 | Epoch | Learning Rate | Hidden Node | Activation | MSE |

| 실험1  |      
| 실험2  |     
| 실험3  |     

실험 결과를 비교하고 가장 성능이 좋은 모델을 선택하시오.

---

## 실습문제 4. 활성화 함수 성능 비교

다음 활성화 함수를 적용하여 성능을 비교하시오.

* Sigmoid
* Tanh
* ReLU
* Softplus

### 작성 내용

| Activation Function | MSE | Correlation |

| Sigmoid                  |    
| Tanh                       |    
| ReLU                     |    
| Softplus                 |    

가장 좋은 성능을 보인 활성화 함수를 선택하고 이유를 설명하시오.

---

## 실습문제 5. 최종 모델 평가 보고서 작성

다음 항목을 포함하여 최종 보고서를 작성하시오.

1. 데이터셋 설명
2. 정규화 방법 설명
3. Model1 구조 설명
4. Model2 구조 설명
5. Model3 구조 설명
6. 손실 함수 설명
7. Optimizer 설명
8. 실험 결과 비교
9. 최종 선택 모델
10. 모델 성능 향상 방안

---

### 추가 도전 과제 : 
하단에 코드셀 추가해서 코드로 작성하고, 코드를 이곳에 복사해서 제출합니다. ==============

#### 도전 과제 1

은닉층을 다음과 같이 변경하여 성능을 비교하시오.

```
hidden_layers=[10,10]
hidden_layers=[20,20]
hidden_layers=[50,50]
```

---

#### 도전 과제 2

Dropout Layer를 추가하여 과적합을 감소시키시오.

---

#### 도전 과제 3

Batch Normalization을 추가하여 성능 변화를 확인하시오.

---

#### 도전 과제 4

학습 과정에서 Epoch별 Loss 그래프를 출력하고 결과를 분석하시오.

---

#### 도전 과제 5

실제값(Actual)과 예측값(Predicted)을 Scatter Plot으로 시각화하고 모델 성능을 분석하시오.
