"""
Write a Python program that checks if a string is a palindrome or not (if it's read the same backwards and forwards).

The program should be case-insensitive. Therefore, "A" should be considered equivalent to "a".

Print True if the string is a palindrome. Else, print False.

If the string is empty, print True.
"""

# option 1

def is_palindrome(string):
    string = string.lower()

    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return is_palindrome(string[1:-1])

print(is_palindrome(""))

# option 2

a = "Anna".lower()
b = a[::-1]

if a == b:
    print("True")
else:
    print("False")
