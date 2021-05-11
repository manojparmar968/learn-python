"""
Write a Python program that checks if the string s ends with a specific sequence of characters denoted by the variable suffix.

If it does, print True. Else, print False.

This test should be case sensitive. Therefore, "A" should not be equivalent to "a".

If the length of the suffix is greater than the length of the string, print False.
"""

s = "Hello"
suffix = "ello"

# option 1

print(s[-len(suffix):] == suffix)

# option 2

print(s.endswith(suffix))