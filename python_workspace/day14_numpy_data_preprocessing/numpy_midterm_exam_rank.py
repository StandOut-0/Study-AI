import numpy as np

score = np.array([90, 80, 70, 60, 100,  50, 40, 40, 20, 10])
print(score.argsort())
desc_index = score.argsort()[::-1]
print(desc_index)

print('------------------------------')
rank = np.empty_like(score)
desc_index = score.argsort()[::-1]
print(desc_index)
rank[desc_index] = np.arange(1, len(score) + 1)
print(rank)