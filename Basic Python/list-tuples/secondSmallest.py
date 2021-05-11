"""
Write a Python program that prints the second smallest value in a list.

If the list is empty or only has one element, print None.

"""
l = [1,2,3,4]

if len(l) > 1:
    new_list = list(set(sorted(l)))
    print(new_list[1])
else:
    print(None)