# # grade calculator
# # task 1
#
# s=int(input("enter score:"))
# grade = None
# if s >= 60 and s <= 100:
#     print("grade is A")
# elif s >=50 and s <= 59:
#     print("grade is b")
# else:
#     print("do again")
#
# # leap year
# leap_yr=int(input("enter yr:"))
# is_leap= False
#
# if (leap_yr % 4 == 0 and leap_yr % 100 != 0) or (leap_yr % 400 == 0):
#     is_leap = True
# else:
#     is_leap = False
#
# print(f"{leap_yr} is {is_leap}")
#
# #-------------------------------------------------------------------
#
# a= int(input("enter side1:"))
# b= float(input("enter side2:"))
# c= int(input("enter side3:"))
#
# if a == b == c:
#     print("it's triangle")
# elif a == b or b == c or a == c:
#     print("two side same")
# else:
#     print("new triangle")
# #----------------------------------------------


#  trying
# num = int(input("enter num:"))
# num1 = int(input("enter num:"))
#
# result= num + num1
# result1= result + result
#
# print(result)
# print(result1)
#-------------

a,b = 0,1
while a < 10:
    print(a, end=" ")
    a,b = b, a+b