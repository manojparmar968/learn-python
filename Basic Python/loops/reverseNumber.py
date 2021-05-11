"""
Write a Python program that prints the digits of a number in reverse order on the same line.

If the number only has one digit, print this digit.

Hints:
To print the digits on the same line without a space in between, 
you can use print(<value>, end="")
"""

n = 1
rev = 0

# while (n > 0):
#     a = n%10
#     rev = rev*10+a
#     n = n // 10
# print(rev)

# option 2
num = 123

reverse = int(str(num)[::-1])
print(reverse)