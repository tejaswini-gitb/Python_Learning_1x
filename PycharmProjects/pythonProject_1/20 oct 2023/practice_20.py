
no=int(input("enter no:\t"))

for i in range(1):
    if no > 45:
        print(" you can enter")
    else:
        print("try again")


#fibonacci series

num=int(input("enter number:"))
a,b=0,1
while a < num:
    print(a,end=' ')
    a,b=b,a+b
    print(" ")

name=input("enter name:")
match name:
    case "tejaswini" , "poorva" ,"pooja":
        print("enter with pass")
    case "12":
        print("pass")