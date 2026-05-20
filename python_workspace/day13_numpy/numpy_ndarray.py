import numpy as np

if False:
    one_dimensional_array = np.array([1, 2, 3, 4, 5])
    print("one_dimensional_array--------------------------------")
    print(one_dimensional_array)

    two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6]])
    print("two_dimensional_array--------------------------------")
    print(two_dimensional_array)

    three_dimensional_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print("three_dimensional_array--------------------------------")
    print(three_dimensional_array)

    print("type ----------------------------------------")
    print(one_dimensional_array.dtype, type(one_dimensional_array))

    print("axis 축, 차원크기 튜플형식, 원소갯수----------------------------------------")
    print(one_dimensional_array,
          one_dimensional_array.ndim, 
          one_dimensional_array.shape, 
          one_dimensional_array.size)
elif False:
    print("arrange ----------------------------------------")
    print(np.arange(2, 10, 2, dtype=np.int32))

    print("empty ----------------------------------------")
    print(np.empty(2, dtype=np.int32))

    print("ones ----------------------------------------")
    print(np.ones(2, dtype=np.int32))

    print("zeros ----------------------------------------")
    print(np.zeros(2, dtype=np.int32))

    print("full ----------------------------------------")
    print(np.full((2, 3), 5))

    print("eye ----------------------------------------")
    print(np.eye(3, dtype=np.int32))
elif False:
    print("dtype and astype ----------------------------------------")
    one_dimensional_array = np.array([1, 2, 3, 4, 5], dtype=np.int32)
    print(one_dimensional_array.astype(np.float32))
elif False:
    print("itemsize and resize and reshpe ----------------------------------------")
    one_dimensional_array = np.array([1, 2, 3, 4, 5], dtype=np.int32)
    print(one_dimensional_array.itemsize)
    print(one_dimensional_array.resize((2, 3)))
    print(one_dimensional_array.reshape((2, 3)))
elif False:    
    print("indexing and shape ----------------------------------------")
    one_dimensional_array = np.array([1, 2, 3, 4, 5, 6], dtype=np.int32)
    print(one_dimensional_array[0])
    print(one_dimensional_array[1:3])
    print(one_dimensional_array.shape)
    one_dimensional_array.shape = (2, 3)
    print(one_dimensional_array)
    print(one_dimensional_array.shape)
elif False:  
    print("eye and identity ----------------------------------------")
    print(np.identity(3, dtype=np.int32), '\n')
    print(np.eye(3, dtype=np.int32), '\n')
    print(np.eye(2, 4, dtype=np.int32), '\n')
    print(np.eye(3, k=2, dtype=np.int32))
elif False:  
    print("linspace ----------------------------------------")
    print(np.linspace(1, 10, 5, dtype=np.int32))

    print("logspace ----------------------------------------")
    print(np.logspace(1, 10, 5, dtype=np.int32))

    print("geomspace ----------------------------------------")
    print(np.geomspace(1, 10, 5, dtype=np.int32))
elif False:  
    print("rand ----------------------------------------")
    print(np.random.rand(2, 2))

    print("randn ----------------------------------------")
    print(np.random.randn(2, 2))

    print("randint ----------------------------------------")
    print(np.random.randint(0, 10, 2, dtype=np.int32))
elif False: 
    print("random ----------------------------------------")
    print(np.random.random(2))

    print("random_sample ----------------------------------------")
    print(np.random.random_sample(2))
    
    print("random_choice ----------------------------------------")
    print(np.random.choice([1, 2, 3, 4, 5], 2, replace=False))
elif True: 

    print("random_integers ----------------------------------------")
    print(np.random.random_integers(0, 10, 2))

    print("random_shuffle ----------------------------------------")
    print(np.random.shuffle([1, 2, 3, 4, 5]))

    print("random ----------------------------------------")
    print(np.random.seed(1))
    print(np.random.rand(2, 2))
    print(np.random.seed(2))
    print(np.random.rand(2, 2))
    print(np.random.seed(1))
    print(np.random.rand(2, 2))

