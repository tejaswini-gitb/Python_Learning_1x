a = 5
a += 6
print(a)

a -= 4
print(a)

a *= 3   # a*a*a output of privious
print(a)

a %= 2
print(a)

list= [1,55,3,4,1,6,6,10]
print(5 in list)
print(55 in list)
print(0.2 not in list)

x=[1,2,3]
y=[1,2,3]
print(x is y) # id are different


print(id(x))
print(id(y))
print(x is not y)

# ternary operator

x=5
y=15

max_val= x if x > y else y
print(max_val)

age= int(input("enter age:"))
result= "yes,you can watch movie" if age > 18 else "not allowded"
print(result)