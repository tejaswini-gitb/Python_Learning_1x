# factorial

# 5!=5*4*3*2*1---- 120
# 3!= 3*2*1 ----6
# 1! =1

number= int(input("enter number: "))
if number < 0:
    print("factorial is not possible")
else:
    fact =1
    for i in range (1, number + 1):
        fact = fact * i
print("fact is -->", fact)

