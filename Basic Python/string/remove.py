"""
Write a Python program that prints a copy of the string s without any spaces.

Words should be connected in the final string.

If the string doesn't contain spaces, print it intact.
"""
import copy

s = "Hello World! "
new_s = ""

# option 1

# set_s = copy.copy(s)
# print(set_s.replace(" ",""))

# option 2

for char in s:
    if char != " ":
        new_s += char
print(new_s)