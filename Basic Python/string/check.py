"""
Write a Python program that checks if the string s contains all the letters in the alphabet (case-insensitive, so "A" should be equivalent to "a").

If it does, print True. Else, print False.

Before comparing the characters, you should convert the string to lowercase.

If the string contains spaces, ignore them before finding the result.

You may assume that the string doesn't contain any other symbols, only spaces (possibly).

Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz'
"""
import string

s = 'Hello'
s1 = 'abcdefghijklmnopqrstuvwxyz'
s2 = 'The quick brown fox jumps over the lazy dog'

# option 1

# print(s==s.lower())

# option 2

# set_s = set(s2.lower())
# if " " in set_s:
#     set_s.remove(" ")
# print(set_s == set(string.ascii_lowercase))

# option 3

# is_panagram = True

# for char in string.ascii_lowercase:
#     if char not in s2.lower():
#         is_panagram = False
# print(is_panagram)

# option 4

is_panagram = True

for char in string.ascii_lowercase:
    if char not in s2.lower():
        is_panagram = False
        break
print(is_panagram)