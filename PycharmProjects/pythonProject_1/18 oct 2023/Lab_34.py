#triangle classifier

side1=float(input('enter side value 1:'))
side2=float(input('enter side value 2:'))
side3=float(input('enter side value 3:'))
if side1 == side2 == side3:
    print("equal")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("ixo")
else:
    print("not equal")