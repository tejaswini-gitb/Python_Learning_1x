#list-----items

my_list=[1,2,5,0,3,0,5,9,10]    # list of integer in [ ]
#........0,1,2,3,4,5,6,7,8
my_list2=[1,True,"Teju","25kop",3.14]   # list of different data types is possible

#indexing
print("initial list:",my_list)
print("initial list2:",my_list2)
print("initial list2:",my_list2[4])
print(my_list[-4])   # 0
#changing an element
my_list[3]=20
print("initial list:",my_list[1])
print("initial list:",my_list)   # before initial list: [1,2,3,5,9,10] after initial list: [1,20,3,5,9,10]

# append
my_list.append(4)   # adding value in the end
print("list after appending:",my_list)

# extend
my_list.extend([5,6])   # extend value with list
print("list after extending:",my_list) # with privious change it extend value

#insert()
my_list.insert(5,'p')   # in position of 5th index , p is inserted
print("list after inserting:",my_list)
print(type(my_list.insert))

# remove()
my_list.remove(9)
print("list after removing:", my_list)
print(type(my_list.remove))

# copy
my_copy_list = my_list .copy()
print(my_copy_list)
print("index of 3 in list:", my_list.index(3)) #index of 3 in list: 2  ___from first list

# clear()
# my_list.clear()
# print("clear list:",my_list) # clear list: []
# print(type(my_list.clear()))

#sort
# my_list.sort()  # sorting doesn't work with mix data types
# print(my_list.sort)

#reverse
my_list.reverse()
print(my_list.reverse())  #try again