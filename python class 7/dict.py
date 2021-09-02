my_dict = {
    "level 1" : 5,
    "level 2" : 10,
    "level 3" : 15
}
print(my_dict["level 3"])

my_dict['level 5'] = 25
print(my_dict)

my_dict['level 2'] = 12
print(my_dict)

my_dict.popitem()
print(my_dict)

my_dict.pop('level 1')
print(my_dict)

my_dict.clear()
print(my_dict)


my_dict = {
    "level 1" : 5,
    "level 2" : 10,
    "level 3" : 15
}

for el in my_dict:
    print(el)

for el in my_dict.items():
    print(el)

for el in my_dict.values():
    print(el)

for k, v in my_dict.items():
    print(k, v)




