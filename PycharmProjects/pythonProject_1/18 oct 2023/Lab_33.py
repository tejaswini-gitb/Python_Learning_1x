year=int(input("enter year:"))
is_leap_yr=False

if ( year %4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
    is_leap_yr = "is leap year"
else:
    is_leap_yr= "not leap year"

print(f"{year} {is_leap_yr}")