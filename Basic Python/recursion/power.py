"""
Write a Python program that find the value of a raised to the power b recursively.

The operation is a**b in Python, where a is the base and b is the exponent.

If the value of b is 0, the result is automatically 1 because every number raised to the power 0 is 1.
"""

def calculate_power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * calculate_power(a, b-1)

print(calculate_power(2, 1))