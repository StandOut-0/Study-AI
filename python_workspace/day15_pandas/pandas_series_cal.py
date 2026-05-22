import pandas as pd

if False:
    score = pd.Series([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])
    print(score)
    print(score*0.2)

score1 = pd.Series([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])
score2 = pd.Series([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])
score3 = pd.Series([100, 90, 80, 70, 60, 50, 40, 30, 20])
# print(score1+ score2)
# print(score1+ score3)
print(score1.add(score3, fill_value=0))
print(score1.sub(score2, fill_value=0))
print(score1.mul(score2, fill_value=0))
print(score1.div(score2, fill_value=0))