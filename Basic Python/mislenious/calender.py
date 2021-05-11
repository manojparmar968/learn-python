"""
Write a Python program that prints the calendar of a given month in a given year.

The user should be able to specify the month and year.

The month must be an integer between 1 and 12.

The year must be a valid integer.

If the values entered by the user are not valid, a descriptive message should be displayed.

Hints:
The built-in calendar module has a month function that you can use to print a calendar by specifying the year and month.
"""

import calendar

print("welcome to your python calender")
year = int(input("Enter the year (with this format YYYY): "))
month = int(input("Now enter the month (1-12): "))

print(calendar.month(year, month))