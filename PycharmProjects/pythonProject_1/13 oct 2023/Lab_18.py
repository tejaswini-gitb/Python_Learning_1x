# identity----- is, is not

# is returns true if both variables are the same object
# is not returns true if both variables are the object

x= [1,2,3]
y= [1,2,3]

print(x is not y)
print(x is y)

print(id(x))
print(id(y))

a =2
b =2
print(a is not b)
print(a is b)