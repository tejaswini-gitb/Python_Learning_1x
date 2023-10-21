#grade calulator

score= int(input("enter the number:\t"))

if  score  >= 90 and score <= 99:
    print("grade is A+")
elif  score  >= 80 and score <= 89:
    print("grade is B+")
elif  score  >= 70 and score <= 79:
    print("grade is C+")
elif  score  >= 60 and score <= 69:
    print("grade is D+")
elif  score  >= 40 and score <= 59:
    print("grade is E+")
elif  score  >= 1 and score <= 39:
    print("grade is Fail")
else:
    print("invalid input")
