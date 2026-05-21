import numpy as np

if False:
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    x = np.array([10, 20, 30])
    print(A.shape)
    print(x.shape)
    print(np.dot(A, x))
    print(A.shape)
    print(x.shape)
    x_reshape = x.reshape(-1, 1)
    print(x_reshape.shape, x_reshape)
    print(A.dtype)
    print(x.dtype)
if False:
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    C = np.array([[9, 8, 7], [6, 5, 4]])
    print(A * B)
    print(np.dot(C, A))
    print(C @ A)
    print(np.dot(A, C))
    print(A * C)
if False:
    V = np.array([[1], [2], [3]])
    a = 10
    print(a*V)
    print(V*a)
if False:
    A = np.array([
        [2, 1], 
        [1, 3]
    ])
    print(np.linalg.det(A))
    B = np.array([7000, 9000])
    result1 = np.linalg.solve(A, B)
    result2 = np.linalg.inv(A) @ B
    print(result1)
    print(result2)
if False:
    A = np.array([
        [2, 1],
        [4, 2]
    ])
    print(np.linalg.det(A))
if False:
    A = np.array([
        [4, 3],
        [3, 2]
    ])
    b = np.array([23, 16])
    invA = np.linalg.inv(A)
    # invA = np.linalg.solve(A, b)
    # print(invA)
    x= np.dot(invA, b)
    print(x)
    print(np.allclose(np.dot(A, x), b))
if False:
    A = np.array([[1, 4, 3], [1, 3, 2]])
    b = np.array([23, 16])
    x = np.linalg.lstsq(A, b, rcond=None)[0]
    print(x)
    print(np.allclose(np.dot(A, x), b))
if False:
    A = np.array([[2, 0], [0, 2]])
    print(np.linalg.det(A))
if False:
    A = np.array([[8, 5, 3], [4, 1, 6], [7, 10, 9]])
    print(np.linalg.det(A))
if True:
    A = np.array([[4, -2], [2, 3]])
    R = np.array([6, 7])
    A_inv = np.linalg.inv(A)
    print(A_inv)
    
    