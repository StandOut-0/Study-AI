import numpy as np


if False:

    print("단항(unary) ufunc ----------------------------------------")
    arr = np.array([-1, -2, -3, -4, -5], dtype=np.int32)
    print(np.abs(arr))

    print(np.sqrt(np.array([1, 4, 9, 16, 25])))
    print(np.square(np.array([1, 2, 3, 4, 5])))
    print(np.exp(np.array([1, 2, 3])))
    print(np.log(np.array([1, 2, 3])))
    print(np.sin(np.array([0, 1, 2])))
    print(np.cos(np.array([0, 1, 2])))
    print(np.tan(np.array([0, 1, 2])))
    print(np.ceil(np.array([1.2, 2.3, 3.7])))
    print(np.floor(np.array([1.2, 2.3, 3.7])))
    print(np.round(np.array([1.2, 2.6, 3.5])))
    print(np.sign(np.array([-10, 0, 10])))
    print(np.all(np.array([1, 2, 3])))
    print(np.any(np.array([0, 0, 1])))
    print(np.isnan(np.array([1, np.nan, 3])))
    print(np.isfinite(np.array([1, np.inf, np.nan])))


elif True:

    print("이항(binary) ufunc ----------------------------------------")
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([5, 4, 3, 2, 1])
    print(np.add(arr1, arr2))
    print(np.subtract(arr1, arr2))
    print(np.multiply(arr1, arr2))
    print(np.divide(arr1, arr2))
    print(np.power(arr1, 2))
    print(np.maximum(arr1, arr2))
    print(np.minimum(arr1, arr2))
    print(np.mod(arr1, 2))
    print(np.greater(arr1, arr2))
    print(np.less(arr1, arr2))
    print(np.equal(arr1, arr2))
    print(np.not_equal(arr1, arr2))
    print(np.logical_and(arr1, arr2))
    print(np.logical_or(arr1, arr2))