"""
Write a Python program that prints the first and last three characters of the string s as a single string.

If the string has less than six characters, print an empty string (blank output).
"""

s = "wonderful"

# option 1

# if len(s) < 6:
#     print("")
# else:
#     print(s[:3]+s[-3:])

# option 2

if len(s) < 6:
    print("")
else:
    print(s[:3]+s[len(s)-3:])