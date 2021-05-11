"""
Write a Python program that prints the multiplication table for a positive integer n.

The values displayed should go from n x 1 up to n x 10 with a descriptive format (as shown below).

Use a loop to implement your solution.

Hints:
Notice the value that is being updated. That should be the value of the loop variable.
"""

n = 3

print(f"===== Multiplication Table of {n} =====")

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")