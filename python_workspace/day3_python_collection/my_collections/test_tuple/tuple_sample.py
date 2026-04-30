tuple = (1, 2, 3, 4, 5)

def make_tuple1():
    # tuple.insert(3, 6)
    # tuple.append(7)
    return tuple
    return 
def typle_indexing():
    return tuple[3]

def tuple_slicing():
    return tuple[1:4:2]

def tuple_tuple():
    return tuple + tuple

def istupe1():
    return (1)

def istupe2():
    return (1,)

def istupe3():
    x = 1, 2, 3
    return x

# 함수에서 튜플로 여러개를 리턴할 수 있다.
def tuplecanreturn():
    return 1, 2, 3

def tuple_builtin():
    txt = ""
    txt = "count: " + str(tuple.count(1))
    txt += "\n"
    txt += "index: " + str(tuple.index(1))
    txt += "\n"
    txt += "length: " + str(len(tuple))
    return txt