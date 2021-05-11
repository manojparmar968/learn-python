"""
Write a Python program that displays the current date and time.

The program should print Current Date and Time: on the previous line.

The date should be formatted as YYYY-MM-DD

The time should be formatted as HH:MM:SS

Hints:
The datetime module has helpful functions to solve this challenge.

The strftime function can also help you format the date and time.
"""

import datetime

current_date_time = datetime.datetime.now()

print("Current date and time: ")
print(current_date_time.strftime("%Y-%m-%d %H:%M:%S"))