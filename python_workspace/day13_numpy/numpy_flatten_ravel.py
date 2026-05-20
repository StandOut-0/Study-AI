import numpy as np

if False:
    print("---------------------------------")
    arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

    f = arr.flatten()
    r = arr.ravel()

    f[0] = 999
    r[1] = 888

    print("flatten:", f)
    print("ravel:", r)
    print("arr:", arr)

