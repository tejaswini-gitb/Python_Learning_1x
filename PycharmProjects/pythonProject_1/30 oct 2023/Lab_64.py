# dict=
my_dict={"a":5,"b":6,"i":8,"f":98,"a":8}
print(my_dict)# latest value of "a" is used, if duplicates is there

keys=my_dict.keys()
print(keys)
print("-----------")
print(list(keys))#1
key_list=list(keys)#2
print(key_list)#2
print(key_list[0])
print(key_list[1])

values=my_dict.values()
print(values)

#my_dict.clear()
#print(my_dict)

copy_my_dict=my_dict.copy()
print(copy_my_dict)
print(set )

print(my_dict.items())
set_dict=set(my_dict.items()) #dict_items([('a', 8), ('b', 6), ('i', 8), ('f', 98)])

print(my_dict.pop('a'))  # delete last entry ,output--->{'b': 6, 'i': 8, 'f': 98}

my_dict["a"]=values
#del my_dict
print(my_dict)

#ordered dict
my_dd={"a":4,"b":8,"c":8,"d":7}
print(my_dd)


from collections import OrderedDict
my_dd= OrderedDict()
my_dd['a']=45
my_dd['c']=75
my_dd['b']=4
my_dd['d']=47

print(my_dd)