def hello():
    print("hello py")

hello()


def functwp(a):
    return a**2

output= functwp(3)
print(output)

#palindrom

def reverse_string(input_string):
    reverse_str = ""
    for char in input_string:
         reverse_str = char + reverse_str
    return reverse_str

original_str = "125351"
rev_str = reverse_string(original_str)
print(rev_str)

if original_str == rev_str:
    print("palindrome")
else:
    print("not p")

# 2

original_str = "tejaswini"
rev_str = original_str[::-1]
print(rev_str)

#3
original_str = "wini"

def rev_string(original_str):
    return ''.join(reversed(original_str))
rev_str=rev_string(original_str)
print(rev_str)

#
num = int(input("enter number:"))
sum=0
while num != 0 :
    digit = num % 10
    sum =sum + digit
    num = int(num/10)
print(sum)

# lambada

output=lambda value:value*3
print(output(2))

say= lambda name:print("hi python".name)
say("nm")