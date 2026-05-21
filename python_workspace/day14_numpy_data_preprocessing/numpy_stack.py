import numpy as np

if False:
    ar1 = np.ones((2, 3))
    ar2 = np.zeros((2, 3))
    print(ar1)
    print(ar2)
    print(np.hstack((ar1, ar2)))
if False:
    ar1 = np.ones((2, 3))
    ar2 = np.zeros((2, 3))
    print(ar1)
    print(ar2)
    print(np.vstack((ar1, ar2)))
if False:
    ar1 = np.ones((2, 3))
    ar2 = np.zeros((2, 3))
    print(ar1)
    print(ar2)
    print(np.dstack((ar1, ar2)))
if False:
    ar1 = np.ones((2, 3))
    ar2 = np.zeros((2, 3))
    # print(ar1)
    # print(ar2)
    print(np.stack((ar1, ar2)))
    print('------------------------------')
    print(np.stack((ar1, ar2), axis=0))
    print('------------------------------')
    print(np.stack((ar1, ar2), axis=1))
    print('------------------------------')
    print(np.stack((ar1, ar2), axis=2))
if False:
    ar1 = np.ones((2, 3))
    ar2 = np.zeros((2, 3))
    cr4 = np.r_[ar1, ar2]
    print(cr4)
if True:
    ar1 = np.ones((2, 3))
    ar2 = np.zeros((2, 3))
    cr4 = np.c_[ar1, ar2]
    print(cr4)
        