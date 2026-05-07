def test1():
    set1 = {1, 2, 3, 7, 3, 3, 4, 5}
    print(f'set1: : {set1}')

    set2 = set()
    print(f'set2: : {set2}')

    set3 = set("Hellolll")
    print(f'set3: : {set3}')

    mylist = [1, 2, 3, 7, 3, 3, 4, 5]
    set4 = set(mylist)
    print(f'set4: : {set4}')

    set5 = list(dict.fromkeys(mylist))
    print(f'set5: : {set5}')

    print('set1+set2: ', set1 & set2) # 정수 사이의 교집합
    print('intersection: ', set1.intersection(set2)) # 일반 정수 사이의 교집합

    print('set1-set2: ', set1 - set2) # 차이
    print('difference: ', set1.difference(set2)) # 차이

    print('set1^set2: ', set1 ^ set2) # 대칭 차이
    print('symmetric_difference: ', set1.symmetric_difference(set2)) # 대칭 차이

    print('set1|set2: ', set1 | set2) # 합집합
    print('union: ', set1.union(set2)) # 합집합

    print('issubset: ', set1.issubset(set2)) # 부분 집합
    print('issuperset: ', set1.issuperset(set2)) # 완전 집합

    set1.add(999) # 추가
    print(set1)

    set1.remove(999) # 제거
    print(set1)

    set1.update([999, 777, 666]) # 업데이트
    print(set1)

    set1.clear() # 지우기
    print(set1)
    



if __name__ == "__main__":  
    test1()