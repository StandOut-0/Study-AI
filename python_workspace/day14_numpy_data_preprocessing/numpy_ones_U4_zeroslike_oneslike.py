import numpy as np

if False:
    er = np.ones((2, 3, 4), dtype='i8')
    print(er.shape)
    print(er)
    print(er.dtype)
if False:
    arr = np.array(["apple", "cat", "hi"], dtype='U4')
    print(arr)
if False:
    arr = np.array(["apple", "cat", "hi"], dtype='U4')
    arr_zero_like = np.zeros_like(arr)
    print(arr_zero_like)
    arr_one_like = np.ones_like(arr)
    print(arr_one_like)