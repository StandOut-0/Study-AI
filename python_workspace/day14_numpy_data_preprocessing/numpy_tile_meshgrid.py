import numpy as np

if False:
    arr = np.array([True, True, True])
    print(np.tile(arr, 3))
    arr = np.array([True, False, True])
    print(np.tile(arr, 3))
if False:
    x = np.arange(3)
    y = np.arange(3)
    metrix_X, metrix_Y = np.meshgrid(x, y)
    print(metrix_X)
    print(metrix_Y)
    grid_xy = [list(zip(x, y)) for x, y in zip(metrix_X, metrix_Y)]
    print(grid_xy)
if True:
    x = np.arange(0, 5)
    y = np.arange(0, 5)
    metrix_X, metrix_Y = np.meshgrid(x, y)
    print(metrix_X)
    print(metrix_Y)