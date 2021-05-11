"""
Write a Python program that prints the string s with the character curr_char replaced by the character new_char.

curr_char and new_char are variables that contain strings with a single character.

You may assume that new_char will not be an empty string.

The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).

If no match is found, print the initial string.
"""
s = "Hello" 
new_s = ""

curr_char = "l"
new_char = "s"

# option 1

# if not new_char:
#     print("new_char cann't be empty")
# else:
#     print(s.replace(curr_char,new_char))

# option 2:

# for char in s:
#     if char == curr_char:
#         new_s += new_char
#     else:
#         new_s += char
# print(new_s)

"""
Write a Python program that prints a version of the string s with all commas replaced by dots.
"""

s1 = "Hello, world!"

print(s1.replace(",","."))