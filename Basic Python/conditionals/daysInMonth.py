"""
Write a Python program that prints the number of days in a given month.

The value of the variable month is the name of the month with the first letter capitalized.

Do not consider leap years for the number of days in February.

You can add a customized message. For example: "<month> has: <num_days> days."

🔸 Hints:
Remember that February has 28 days.
"""

month = "February"
month_31_days = ("January","March","May","July","August","October","December")
month_30_days = ("April","June","September","November")

if month in month_31_days:
    print(f"{month} has: 31 days")
elif month in month_30_days:
    print(f"{month} has: 30 days")
else:
    print(f"{month} has: 28 days")
