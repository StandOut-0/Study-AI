import numpy as np


ar = np.array([1, 2, 3, 4, 5])
idx_array = np.array([True, False, True, False, True])
ar[idx_array]

print(ar[idx_array])