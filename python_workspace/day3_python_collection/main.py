import my_collections.test_list.list1_index_slice as list1
import my_collections.test_list.list2_insert_append_remove_pop_extend_reverse_sort_count as list2
# from my_collections.test_list.list_sample import make_list1



if __name__ == "__main__":
    print("start---------------------------------")

    whatfile = "list2"
    
    if whatfile == "list1":
        print(list1.make_list1())
        # print(list1.make_list())
        # print(make_list1())
        print(list1.make_list1())
        print(list1.make_list2())
        print(id(list1.make_list1()))
        print(id(list1.make_list2()))

        print(list1.list_indexing()[3])
        print(list1.list_indexing())

        print(list1.list_slicing())
    elif whatfile == "list2":
        print(list2.lst)
        print(list2.list_insert())
        print(list2.list_append())
        print(list2.list_remove())
        print(list2.list_pop())
        print(list2.list_extend())
        print(list2.list_reverse())
        print(list2.list_sort())
        print(list2.list_count())

    print("end---------------------------------")