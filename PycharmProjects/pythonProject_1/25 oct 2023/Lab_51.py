data=[1,2,8,5,6,10,8,8,0]
print(data)
print(data.sort())

#data1=[True,1,'yo',52,52,100]
#data1.sort()
#print(data1) #TypeError: '<' not supported between instances of 'str' and 'int'


data=[1,2,5,78,3,5]
l=data
l2=data.copy()

print(data)
print(l)
print(l2)

data[1]=505
print(data)
