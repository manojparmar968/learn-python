"""
Write a Python program that prints the second largest value in a list.

If the list is empty or only has one element, print None.
"""

l = [4,1,5,8,3,7,2,8]
# l = [4]

# option 1

if len(l) == 0 or len(l) == 1:
    print(None)
else:
    list_sort = list(set(sorted(l)))
    print(list_sort[-2])

# option 2

if len(l) > 1:
    list_sort = list(set(sorted(l)))
    print(list_sort[-2])
else:
    print(None)