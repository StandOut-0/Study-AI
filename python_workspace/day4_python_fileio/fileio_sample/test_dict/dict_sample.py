
def dict_test1():
    dict1 = dict()
    print(dict1, type(dict1))
    
    dict2 = {}
    print(dict2, type(dict2))

def dict_test2():
    dict1 = {'a':1, 'b':2, 'c':3}
    print(dict1, type(dict1))

    dict2 = {1:'Python', 2:[1, 2, 3], 3:('Hi', 'im', 6)}
    print(dict2, type(dict2))

    dict2[2][2] = 4
    dict2[2].append(8)
    dict2[4] = 'Bye'
    print(dict2)

def dict_test_function():
    '함수이름 바로밑에 입력하는 이 문구는 설명하는 문자열'
    dict1 = {
        'a':1,
        'b':2,
        'c':3
    }
    print('key목록', dict1.keys())
    print('value목록', dict1.values())
    print('item목록', dict1.items())

    dict2 = {
        'a':111,
        'B':2,
        'C':3
    }

    dict1.update(dict2)
    print(dict1)

    poptodict = dict1.pop('a')
    print(poptodict)
    print(dict1)

    print('dict2: ',dict2)
    dict3 = dict2.copy()
    print('dict3: ',dict3)
    dict2.clear()
    print('dict2: ',dict2)

    dict4 = dict3
    print('dict2: ',dict2, id(dict2))
    print('dict3: ',dict3, id(dict3))
    print('dict4: ',dict4, id(dict4))


    print('a' in dict4)

    print(111 in dict4.values())

    # print('사전변수[키]: ',dict4['adddd'])
    print('사전변수.get:',dict4.get('adddddd'))

    print('삭제전: ', dict4)
    del dict4['a']
    print('삭제후: ', dict4)


if __name__ == '__main__':
    dict_test1()
    dict_test2()
    dict_test_function()