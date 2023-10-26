#list-----items

my_list=[1,2,3,5,9,10]    # list of integer
my_list2=[1,True,"Teju"]   # list of different data types

#indexing
print("initial list:",my_list)
print("initial list:",my_list[0])

#changing an element
my_list[1]=20
print("initial list:",my_list[1])
print("initial list:",my_list)   # before initial list: [1, 2, 3] after initial list: [1, 20, 3]

# append
my_list.append(4)   # adding value in the end
print("list after appending:",my_list)

# extend
my_list.extend([5,6])   # extend value with list
print("list after extending:",my_list)

#insert()
my_list.insert(5,'o')   # in position of 1 , 2 is inserted
print("list after inserting:",my_list)
print(type(my_list.insert))

# remove()
my_list.remove(4)
print("list after removing:",my_list)
print(type(my_list.remove))

# copy
my_copy_list=my_list.copy()
print(my_copy_list)
print("index of 3 in list:",my_list.index(3))

# clear()
my_list.clear()
print("clear list:",my_list) # clear list: []
print(type(my_list.clear()))

#sort
my_copy_list.sort()
print(my_list.copy)

#reverse
my_copy_list.reverse()
print(my_copy_list)