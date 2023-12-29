# try except

try:
    a = 10 / 0
except ZeroDivisionError as e :
    print(e)

# try except and nested except
# else and finally

try:

    num1 = int(input("enter a number 1 :"))
    num2 = int(input("enter a number 2 :"))

    result = num1 / num2

except ValueError:
    print("invalid error")
except ZeroDivisionError:
    print("num 2 is zero")
else:
    print(f" result= {result}")
finally:
    print(" num. will be excecuted ")