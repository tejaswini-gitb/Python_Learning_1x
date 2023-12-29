import math

radius=float(input("enter radius:\t "))
print(radius)
area= 3.14 * (radius ** 2)
print(area)


no1= int(input('enter no1:\t'))
no2= int(input('enter no2:\t'))
result1= "no1 is greater" if no1 > no2  else "---"
result2= "no2 is greater" if no2 > no1  else "-- "
result3= "same value" if no1 == no2 else ""
print(result1)
print(result2)
print(result3)


no1= float(input('enter no1:\t'))
no2= float(input('enter no2:\t'))
no3= float(input('enter no3:\t'))
result1= no1 if (no1 > no2 and no1 > no3 ) else (no2 if no2 > no3 else no3)
print(result1)


a1=int(input("enter number:\t"))
print(a1)
square=(a1 ** 2)
cube=(a1 ** 3)
print(square)
print(cube)
