"""
Write a Python program that prints a list with the elements that listA and listB have in common.

If they don't have any elements in common, print an empty list.

The program should not assume that the lists have the same length.

You may assume that each element will only appear once in each list.
"""

listA = [1,2,3]
listB = [1,2,3]
new_list = []

for elem in listA:
    if elem in listB:
        new_list.append(elem)
print(new_list)
