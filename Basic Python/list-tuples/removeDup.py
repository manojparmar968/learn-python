"""
Write a Python program that removes duplicate elements from a list, only keeping one occurrence of each element in the list.

The original list should be mutated (modified).

The program must print the final version of the list.

Hints:
Sets are commonly used to remove duplicates from lists and tuples in Python.
"""

s = ["a","B","c","a","b","a","d","e","f","b","f"]

# option 1

duplicate_remove = sorted(list(set(s)))
print(duplicate_remove)

# option 2

no_duplicate = list(dict.fromkeys(s))
print(no_duplicate)