"""
Write a Python program that adds a new key-value pair to a dictionary only if the key doesn't exist already.

If the key-value pair exists in the dictionary, do not update the existing value. The dictionary should not be modified in this case.

Store the new key in the new_key variable and the new value in the new_value variable.

Print the final value of the dictionary.

Hints:
You can use the not in operator to check if a key is not in a dictionary.
"""

d = {"a":1,"b":2,"c":3,"e":5}
key = "d"
value = 4

# option 1

if key not in d:
    d[key] = value
    print(d)
else:
    print(d)

# option 2, it will update the value of dict

# d[key] = value
# print(d)