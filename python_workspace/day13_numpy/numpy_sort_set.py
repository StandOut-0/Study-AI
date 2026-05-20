import numpy as np

if False:
    arr = np.array([1, 2, 3, 4, 5])
    print(arr[np.argsort(arr)])
    print(np.sort(arr))
    print(arr[np.argsort(arr)])
    print(np.sort(arr))
elif True:
    print(np.unique(np.array([1, 1, 1, 2, 3, 4, 5, 900,  6, 7, 8, 9, 10])))
    print(np.intersect1d(np.array([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 
                         np.array([1, 2, 3, 4, 5, 900,  6, 7, 8, 9, 10])))
    print(np.union1d(np.array([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                     np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    # 버전 업데이트로 제거된 함수 in1d
    print(np.isin(np.array([1, 1, 1, 2, 3, 4, 900, 5, 6, 7, 8, 9, 10]),
                 np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    print(np.setdiff1d(np.array([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 900, 10]),
                       np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    print(np.setxor1d(np.array([1, 1, 1, 2, 3, 4, 900, 5, 6, 7, 8, 9, 10]),
                      np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
