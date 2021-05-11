"""
Write a Python program that prints the smallest of three integers a, b, and c.
"""

a = 1
b = 3
c = 4

# option 1

if (a <= b) and (a <= c):
    print(a)
elif (b <= a) and (b <= c):
    print(b)
else:
    print(c)

# option 2

print(min(a,b,c))