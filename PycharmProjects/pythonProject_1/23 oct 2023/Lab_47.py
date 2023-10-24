# sum of numbers
# e.g -----int( 12345 )==== 1+2+3+4+5==== 15
# 12345==== float( 1+2+3+4+5) ==== 16.666666


############## 1
num=float(input("enter number:"))
sum = 0
while num != 0:
    digit = num % 10
    sum = sum + digit
    num = float(num / 10)

print(sum)

############ 2

num=int(input("enter number:"))
sum = 0
while num != 0:
    digit = num % 10
    sum = sum + digit
    num //= 10

print(sum)