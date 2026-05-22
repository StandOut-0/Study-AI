import numpy as np
import pandas as pd

if False:

    dic = {'name':['hong', 'lee', 'kim', 'john'], 'age':[20, 30, 40, 50]}
    stud_label = pd.Index(['name1', 'age1'])
    ser = pd.Series(dic)
    ser.index = stud_label
    print(ser)

    df = pd.DataFrame(dic)
    stud_id = pd.Index(['s1', 's2', 's3', 's4'])
    df.index = stud_id
    print(df)


    df.append(ser)
    print(df)

    idx = pd.Index(['hong', 'lee', 'kim', 'john'])
    print(idx, type(idx))
    print('size: ', idx.size)
    print('shape: ', idx.shape)
    print('dtype: ', idx.dtype)
    print('to_list: ', idx.to_list())
    print('values: ', idx.values)

    print('-'*50)

    print('hong' in idx)
    print(idx.get_loc('hong'))
    print(idx[1:3])

    print('-'*50)

    idx2 = pd.Index(['park'])
    new_idx = idx.append(idx2)
    print(new_idx)

    new_idx = new_idx.insert(1, 'song')
    print(new_idx)

    a = pd.Index(['a', 'b', 'c'])
    b = pd.Index(['b', 'c', 'd'])
    print(a.union(b))
    print(a.intersection(b))
    print(a.difference(b))

dup = pd.Index(['a', 'b', 'c', 'a'])
print('sort_values: ', dup.sort_values())
print('is_monotonic_increasing: ', dup.is_monotonic_increasing)
print('is_monotonic_decreasing: ', dup.is_monotonic_decreasing)
print('is_monotonic_increasing: ', dup.sort_values().is_monotonic_increasing)
print('is_monotonic_decreasing: ', dup.sort_values().is_monotonic_decreasing)

print('unique: ', dup.unique())
print('is_unique: ', dup.is_unique)
print('isin: ', dup.isin(['a', 'b', 'c']))

print('-'*50)

print(dup.drop('a'))
print(dup.delete(1))

print('-'*50)

