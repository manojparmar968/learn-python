"""
Write a Python program to convert a string s to lowercase, sort the characters of each word in alphabetical order, and print the resulting string.

You may assume that the string only contains letters and spaces to separate the words.

Spaces should be preserved in the final string.

Hints:
In Python, uppercase letters come before lowercase letters in alphabetical order.

The sorted() function can be used to get a sorted list with the characters in a string.
"""

s = "Hello World"
new_s = ""

words_list = s.split(" ")

# option 1

# for word in words_list:
#     lowercase_word = word.lower()
#     sorted_word = "".join(sorted(lowercase_word))
#     new_s += sorted_word + " "
# new_s.rstrip()
# print(new_s)

# option 2

for word in words_list:
    new_s += "".join(sorted(word.lower())) + " "
new_s.rstrip()
print(new_s)