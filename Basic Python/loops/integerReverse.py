"""
Write a Python program that prints the integers between a given number n and 1 (in descending order, both inclusive).

The value of n should be entered by the user and you may assume that it is an integer greater than or equal to 1.

Use a loop to print each number on a separate line.

Hints:
The range() function can take a third parameter to specify the step and this step can be negative to decrement the value of the loop variable in every iteration.
"""

n = 6

# option 1

for i in range(n,0,-1):
    print(i)

# option 2

for i in reversed(range(1, n+1)):
    print(i)