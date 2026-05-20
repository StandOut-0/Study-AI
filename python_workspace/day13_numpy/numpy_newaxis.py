import numpy as np

arr = np.array([1, 2, 3])
print(arr.shape)
print(arr[:, np.newaxis])
print(arr[:, np.newaxis].shape)
print(arr[np.newaxis, :])
print(arr[np.newaxis, :].shape)
    