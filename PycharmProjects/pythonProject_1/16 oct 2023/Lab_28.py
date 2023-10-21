# compare two numbers

num1=int(input("enter the num_1:\t"))
num2=int(input("enter the num_2:\t"))
result= "greater than " if num1 > num2 else "less than" if num1 < num2 else "equal to "
print (f"{num1} is {result} {num2}")