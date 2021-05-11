"""
Write a Python program that prints the smallest value in a dictionary.

If the dictionary is empty, print None.

You may assume that the values are numeric.
"""

d = {"a":4,"b":3,"c":7}
if d:
    min_value = min(set(d.values()))
    print(min_value)
else:
    print(None)