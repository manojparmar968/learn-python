"""
Write a Python program that prints if a given year was (or will) be a leap year.

Tip: A leap year is "a year, occurring once every four years, that has 366 days including February 29 as an intercalary day." (Definition by Oxford Languages).

This is how you can determine if a year is a leap year or not:

if (year is not divisible by 4) then (it is a common year).

else if (year is not divisible by 100) then (it is a leap year)

else if (year is not divisible by 400) then (it is a common year)

else (it is a leap year)
"""

year = 1836

# option 1

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# option 2

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# option 3

if year % 4 != 0:
    print(f"{year} is not a leap year")
elif year % 100 != 0:
    print(f"{year} is a leap year")
elif year % 400 != 0:
    print(f"{year} is not a leap year")
else:
    print(f"{year} is a leap year")