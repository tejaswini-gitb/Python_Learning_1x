# Fibnocci series
# 0 1 1 2 3 5 8 13.......

number =int(input("enter the number \n"))

a, b= 0, 1
while a <= number:
    print(a, end =" ")
    a, b = b, a + b