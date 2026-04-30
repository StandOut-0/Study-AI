NAME = "박상희"
name = "park sanghee"
Name = "PSH"
# Name-a = "PSH-"
_name = "underscore name"

print(NAME, name, Name, _name, sep='\n')
# print(NAME, name, Name, type(Name), Name-a, type(Name-a), _name, type(_name), sep='\n')

import keyword
print(len(keyword.kwlist))
print(keyword.kwlist)
print(keyword.iskeyword('if'))