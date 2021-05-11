"""
Write a Python program that calculates and prints the sum of the digits of a positive integer num.

The program must find the sum recursively.

If the integer has only one digit, print the integer as the total sum.
"""

def sum_of_digit(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_of_digit(num // 10)

print(sum_of_digit(1234))