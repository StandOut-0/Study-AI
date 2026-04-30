# collections\test_list\list_sample.py

def make_list1():
    return [1, 2, 3, 4, 5]

def make_list2():
    imlist = list()
    imlist.append(1)
    imlist.append(2)
    imlist.append(3)
    imlist.append(4)
    imlist.append(5)
    return imlist

def list_indexing():
    list = [1, 2, "Python", 3.14, [1, 2, 3]]
    list.insert(3, "Java")
    list.append("C++")
    list[5].append(4)
    return list

def list_slicing():
    list = [1, 2, 3, 4, 5]
    return list[1:4], list [:1], list[2:], list[1], list[-1], list[:]