"""
Write a Python program that prints Floyd's Triangle with n number of rows.

The value of n should be entered by the user. You may assume that it is a positive integer.

Floyd's Triangle is made with consecutive numbers that fill the rows of the triangle (as shown below).
"""

n = 5

count = 1

for i in range(1,n+1):
    for j in range(0,i):
        print(count, end=" ")
        count += 1

    print()