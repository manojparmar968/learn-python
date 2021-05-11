"""
Write a Python program that creates a dictionary from the values contained in nested lists.

Each nested list has this format [value1, value2].

value1 should be the key in the dictionary and value2 should be its corresponding value.

If there are no nested lists, print an empty dictionary.
"""

l = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]

dict1 = {}

for nested_list in l:
    key = nested_list[0]
    value = nested_list[1]
    dict1[key] = value
print(dict1)