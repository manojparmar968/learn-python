"""
Write a Python program that calculates and prints the value of the factorial of the number num using recursion.

The factorial of a number x is denoted by x! and it is equal to x * (x-1) * (x-2) * ... * 1, the product of all positive integers less than or equal to the number.

The value of 0! is equal to 1 by mathematical convention.

Hints:
Remember that the recursive process should stop when the value of num reaches 1.

Try not to test this program with large values because the value of the result increases very quickly as the value of num increases. 
The program may require a lot of time to reach the final solution.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
