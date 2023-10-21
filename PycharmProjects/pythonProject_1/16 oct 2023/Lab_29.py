# find the max num of three num using ternary operator

num1=int(input("enter the num_1:\t"))
num2=int(input("enter the num_2:\t"))
num3=int(input("enter the num_3:\t"))

max_num= num1 if(num1 > num2 and num1 > num3 )else (num2 if num2 > num3 else num3)
print(f"max_num of {num1},{num2} and {num3} is : {max_num}")