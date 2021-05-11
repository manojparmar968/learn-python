"""
Write a Python program that prints "Equal" if three numbers a, b, and c are equal.

If at least one number if different, the program should print "Not Equal"
"""

a = 3
b = 5
c = 3

# option 1

if a == b == c:
    print("Equal")
else:
    print("Not Equal")

# option 2

if (a == b) and (b == c):
    print("Equal")
else:
    print("Not Equal")