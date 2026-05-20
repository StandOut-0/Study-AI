import numpy as np

if False:
    cvt = np.arange(10)
    cvt.shape = (len(cvt), 1)
    print(cvt)
elif True:
    print(np.linspace(1, 10, 10, endpoint=False))
    print(np.linspace(1, 10, 9, endpoint=True))