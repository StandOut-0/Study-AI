import numpy as np

if False:
    x1 = np.array([1, 2, 3, 4, 5])
    print(x1.dtype)
    print(type(x1))
if False:
    x3 = np.array([1, 2, 3], dtype="f")
    print(x3.dtype, x3)
    print(x3[0] + x3[1])

    print("------------------------------")
    x4 = np.array([1, 2, 3], dtype="U")
    print(x4.dtype, x4)
    print(x4[0] + x4[1])
if False:
    print(np.array([0, 1, -1, 0]) / np.array([1, 0, 0, 0]))
    print(np.log(0))
    print(np.exp(-np.inf))
