lst = [1, 3.5, 5, 'list', True, 20, ['a', 'b', 'c']]

def list_insert():
    lst.insert(2, 3)
    return lst

def list_append():
    lst.append(4)
    return lst

def list_remove():
    # 해당되는 값이 여러개일경우
    lst.append(4)
    lst.remove(4)

    # 모든 4를 지우려면
    lst.append(4)
    while 4 in lst:
        lst.remove(4)

    # 모든 데이터를 지우려면
    lst.clear()
    return lst

def list_pop():
    lst.append(4)
    lst.append(5)
    lst.pop() # 마지막 요소 제거

    lst.append(6) 
    lst.append(7)
    impop = "impop"+str(lst.pop(2)) # 인덱스 2에 있는 요소 제거
    lst.append(impop)
    return lst

def list_extend():
    lst2 = [8, 9, 10]
    lst.extend(lst2)
    return lst

def list_reverse():
    lst.reverse()
    return lst  

def list_sort():
    lst.clear()
    lst.extend([5, 2, 9, 1, 3])
    lst.reverse()
    lst.sort()
    lst.sort(reverse=True)
    return lst  

def list_count():
    lst.clear()
    lst.extend([1, 2, 3, 2, 4, 2, 5])
    count_2 = lst.count(2)
    return count_2