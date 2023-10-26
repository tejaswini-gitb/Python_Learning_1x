#1 ----- Count vowels and consonants in a String
#vowels= a e i o u

user = input("Enter your word :")

vowels = ("a","e","i","o","u")
count = 0

for i in vowels:
    for j in user:
        if i == j:
            count = count + 1

print(f"Your vowels count is: {count}")

#2 ------- Right Triangle Star Pattern

#*
#**
#***
#****
#*****

i=0
j=i+1
for i in range (0,5):
    for j in range(0,i+1):
        print ("*",end="")
    print("\r")

"""
a=10
b=5

print(a^b)
"""

#Create a Function with a Parameter which can do x^y

x=int(input("Enter x : "))
y=int(input("Enter y : "))
print(x^y)

def calculate(x,y):
    return x^y

cal=calculate(x,y)
print(f'{x}^{y} is : {cal}')

# Create a Lambda expression to triple power 2**3 a number

task3=lambda x:y**2
print(task3(3))
