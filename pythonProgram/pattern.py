"""
    *****
    ****
    ***
    **
    *
"""
n= 5

for i in range(0,n+1):
    for j in range(1, n-i+1):
        print("*",end="")
    print()


## Using Recursion

def print_pattern(n):
    if n == 1:
        print("*")
    else:
        print("*" * n)
        print_pattern(n - 1)

print_pattern(8)