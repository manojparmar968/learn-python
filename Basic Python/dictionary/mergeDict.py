"""
Write a Python program that merges two dictionaries and prints the resulting dictionary.

"Merging" the dictionaries involves making a new dictionary with the key-value pairs in both dictionaries.

Hints:
Notice that the key-value pairs that share the same key on both dictionaries are not repeated. 
They are updated with the value of the second dictionary.

There is a Python operator that you can use to merge two or more dictionaries.
"""

dict1 = {"a":1,"b":2,"c":3}
dict2 = {"c":4,"d":5,"e":6}

result = dict1 | dict2
print(result)