import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr[np.where(arr > 4)])
arr[np.where(arr > 3)] = 0
print(arr)