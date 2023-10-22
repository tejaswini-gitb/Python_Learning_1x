score =int(input("enter the score: "))

if score >=100 and score <= 125:
    print(" passed with A")
elif score >=80 and score <= 99:
    print(" passed with B")
elif score >=60 and score <= 79:
    print(" passed with C")
elif score >=40 and score <= 59:
    print(" passed with D")
elif score >=30 and score <= 39:
    print(" passed with E")
else:
    print("Failed")