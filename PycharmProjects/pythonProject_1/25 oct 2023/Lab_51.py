#data=[1,2,3,5,6,7,8,8]
#data1=[True,1,'yo',52,52,100]
#data1.sort()
#print(data1) # TypeError: '<' not supported between instances of 'str' and 'int'


data=[1,2,5,78,3,5]
l=data
l2=data.copy()

print(data)
print(l)
print(l2)
data[1]=55
print(data)
print(l)
print(l2)