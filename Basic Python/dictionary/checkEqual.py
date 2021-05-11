"""
Write a Python program that checks if all values in a dictionary are equal.

If they are, print True. Else, print False.

If the dictionary is empty, print "Empty".

Hints:
Loops will be very helpful to solve this challenge. 
You could also make a set from the dictionary to keep only one copy per value.

The .values() method returns the values in a dictionary.
"""

d = {"a":4, "b":4, "c":4}
val = len(set(d.values()))

if val == 0:
    print("Empty")
elif val == 1:
    print("True")
else:
    print("False")