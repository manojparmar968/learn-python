"""
Write a Python program that prints the pattern of asterisks shown below for a given value of n.

The program must include a recursive function.

n represents the number of rows in the resulting pattern and the number of asterisks printed on the first row.
"""

n = 5

for i in range(0,n):
    for j in range(1, n-i+1):
        print("*",end="")
    print()


# option 2

def print_pattern(n):
    if n == 1:
        print("*")
    else:
        print("*" * n)
        print_pattern(n - 1)

print_pattern(8)