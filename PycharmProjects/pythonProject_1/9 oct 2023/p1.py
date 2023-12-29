name = "tejasWINI"

result=name.capitalize()
print(result)

result1=name.lower()
print(result1)

result2=name.upper()
print(result2)

result3=name.swapcase()
print(result3)

result4=name.title()
print(result4)

result5=name.replace("asWINI","MBENZ")
print(result5)

result6=name.find("WINI")
print(result6)

result7=name.count("I")
print(result7)

val = None
print(val)
print(type(val))
print(id(val))
#print(len(val)) #TypeError: object of type 'NoneType' has no len()

# val1 = None + 2  ------TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# print(val1)

list=["ipad","2iphone","mbenz","iwatch","ipod",31,True]
print(list)
print(list[0])
print(list[2])
print(list[4])
print(list[1])
print(len(list))
print(type(list))

print("hello python \\")  # escape char
print("hello python \"hello\"")
print("hello py\nhello" )
print("hello py\thello" )

string= "i like %s" % "python"
print(string)  # replace word

# string1=input("enter name: \n")
# print("your name is %s" % string1)

mlist={"jbh",4,4,"ko",44,"kj"}
print(mlist)
print(type(mlist))

number= {1, 5, 5, 66, 1}   # set no duplicates
print(number)

#1
n1=("2*1=", format(2*1))
n2=("2*2=", format(2*2))
n3=("2*3=", format(2*3))
n4=("2*4=", format(2*4))
n5=("2*5=", format(2*5))
n6=("2*6=", format(2*6))
n7=("2*7=", format(2*7))
n8=("2*8=", format(2*8))
n9=("2*9=", format(2*9))
n10=("2*10=", format(2*10))

print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)
print(n8)
print(n9)
print(n10)

#2
n=int(input("enter no.:"))

print(f'table of {n} is:')
print(f'{n}X1,{n*1}')
print(f'{n}X2,{n*2}')
print(f'{n}X3,{n*3}')
print(f'{n}X4,{n*4}')
print(f'{n}X5,{n*5}')
print(f'{n}X6,{n*6}')
print(f'{n}X7,{n*7}')
print(f'{n}X8,{n*8}')
print(f'{n}X9,{n*9}')
print(f'{n}X10,{n*10}')