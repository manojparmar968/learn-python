"""
Write a Python program that multiplies all the items in a list by the value of the variable factor.

The program must print the list as the output.

The program should also allow multiplying the variable factor by a string in case the list contains strings.

You may assume that the value of factor will be a positive integer.
"""

num = [3,4,5,6]
s = ["a","b","c"]
factor = 2

# option 1

for i in range(len(s)):
    s[i] *= factor
print(s)

# option 2

for i, element in enumerate(num): # enumerate returns a index of a list sequence
    num[i] = element * factor
print(num)