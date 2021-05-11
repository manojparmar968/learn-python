"""
Write a Python program that prints the largest value in a dictionary.

If the dictionary is empty, print None.

You may assume that the values are numeric.
"""

d = {"a":4,"b":3,"c":7}
if d:
    max_value = max(set(d.values()))
    print(max_value)
else:
    print(None)
