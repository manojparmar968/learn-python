"""
Write a Python program that prints a string reversed using a loop.

All the characters must be on the same line in reverse order.

"""

s = "Hello"
str = ""

for i in s:
    str = i+str
print(str)

# option 2

for char in s[::-1]:
    print(char, end = "")

# option 3

for char in reversed(s):
    print(char, end = "")