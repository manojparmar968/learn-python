"""
Write a Python program that checks if the string s starts with the sequence of characters denoted by the variable prefix.

If it does, print True. Else, print False.

This test should be case sensitive. For example, "A" should not be equivalent to "a".

If the length of the prefix is greater than the length of the string, print False.
"""

s = "Hello"
prefix = "He"

# option 1

print(s[:len(prefix)] == prefix)

# option 2

print(s.startswith(prefix))