#list
list=[25,56,35,55,55,14,12,14,56,78]
print(len(list)) #10

#print unique items

set1=set(list)
print(set(list)) #{35, 12, 14, 78, 55, 56, 25}

t=("abc","xyz","lmn","otp")
print('\n set with the use of tuple: ')
print(set(t))

set1={1,2,3}
set2={4,5,6}
set12=set1.union(set2)
print(set12)#{1, 2, 3, 4, 5, 6}

#intersection

set1={1,2,3,7,9}
set2={4,5,6,1,8,7,6}
set12=set1.intersection(set2)
print(set12)  # {1,7}

#difference
set1={1,2,3,4,5.7}
set2={4,5,1,5,6}
set12=set1.difference(set2)
set21=set2.difference(set1)
print(set12) #{2, 3, 5.7}
print(set21) #{5,6}

#subset

set1={1,2,6,4,7,9}
set2={2,1,6}
set12=set1.issubset(set2)
set21=set2.issubset(set1)
print(set12) #false
print(set21) #true


