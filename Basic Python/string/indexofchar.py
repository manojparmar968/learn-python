"""
Write a Python program that prints the character at index i in the string s.

If the index is out of range, the program should print "i is out of range"

If the string is empty, the program should print "Empty String"
"""

s = "hello"
i = 2

# Method 1

# if len(s) == 0:
#     print("Empty String")
# elif i < len(s):
#     print(s[i])
# else:
#     print("i is out of range")

#  Method 2

if not s:
    print("Empty String")
elif i < len(s):
    print(s[i])
else:
    print("i is out of range")
