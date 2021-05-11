"""
Write a Python program that prints the largest and smallest values in a list

Print the two values on the same line, separated by a space.

The largest value should appear first and the smallest value should appear second.

You may assume that the list only contains numeric values.

If the list is empty, print None.
"""

num = [3,4,5,6]

if len(num) == 0:
    print(None)
else:
    new_list = sorted(num)
    print(new_list[:1] + new_list[-1:])

# option 1

# if num:
#     print(max(num), min(num))
# else:
#     print(None)