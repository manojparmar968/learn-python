"""
Write a Python program that converts seconds to minutes and hours.

Present the minutes as an integer and the hours as a decimal value.

Hints:
Remember that 1 hour has 60 minutes and 1 minute has 60 seconds.
"""

seconds = 5400
minutes = seconds // 60
hours = minutes / 60

print(seconds, "is equivalent to:")
print(minutes, "minutes")
print(hours, "hours")