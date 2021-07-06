"""
Write a Python program that prints the string s without the characters located at even indices.

If the string is empty or only has one character, print it intact.
"""

s = "wonderful"
str = ""

# option 1

if len(s) == 0:
    print("")
else:
    for i in range(len(s)):
        if i%2 != 0:
            str = str+s[i]
    print(str)

# option 2

for i in range(1, len(s), 2):
    str += s[i]
print(str)