import my_collections.test_list.list1_index_slice as ls
# from my_collections.test_list.list_sample import make_list1



if __name__ == "__main__":
    print("start")
    
    # print(ls.make_list())
    # print(make_list1())
    print(ls.make_list1())
    print(ls.make_list2())
    print(id(ls.make_list1()))
    print(id(ls.make_list2()))

    print(ls.list_indexing()[3])
    print(ls.list_indexing())

    print(ls.list_slicing())

    print("end")