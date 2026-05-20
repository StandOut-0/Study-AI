import numpy as np
arr = np.array([1, 2, 3, 4, 5])
if False:
    print(np.max(arr)     )
    print(np.min(arr)     )
    print(np.mean(arr)    )
    print(np.median(arr)  )    
elif False:
    print(np.percentile(arr, 50)  )
    print(np.percentile(arr, 25)  )
    print(np.percentile(arr, 75)  )
    print(np.percentile(arr, 90)  )
    print(np.percentile(arr, 100) )
elif False:
    print(np.std(arr) )
    print(np.var(arr) )
elif False:
    print(np.sum(arr)   )
    print(np.prod(arr)  )
elif True:
    x = np.array([1,2,3,4])
    y = np.array([2,4,6,8])

    print(np.cov(x, y))
    print(np.corrcoef(x, y))

    print("---------------------------------")
    i = [1, 2, 3, 4]
    j = [7, 1, 9, 3]
    print(np.cov(i, j))
    print(np.corrcoef(i, j))
