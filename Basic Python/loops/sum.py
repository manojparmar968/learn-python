"""
Write a Python program that calculates and prints the sum of the first 100 non-negative integers (from 1 to 100).

Use a loop to find this sum.

Hints:
sum is a special word in Python used to refer to a function. 
Please do not use it as the name of the variable.
"""

total = 0

for i in range(1, 101):
    total += i
print(total)