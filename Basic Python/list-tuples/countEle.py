"""
Write a Python program that counts the number of elements in a list with value greater than 3.

You may assume that the list only contains numbers.

Print the final count.

Hints:
You will need to define a variable that will act as the counter and print the value of this counter.

"Greater than" means strictly greater than a value. It does not include cases where the value is equal to 3.

You may want to use a for loop, list comprehension, or generator expressions.
"""

num = [1,-1,0,2,2,3]
# num = [1,2,3,4,7,8,9,10]
cou = 0

# option 1

for i in range(len(num)):
    if num[i] > 3:
        cou += 1
print(cou)

# option 2

for i in num:
    if i > 3:
        cou += 1
print(cou)