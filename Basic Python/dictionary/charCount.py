"""
Write a Python program that creates and displays a dictionary that maps each letter in a string to how many times the character occurs in the string (its frequency).

The dictionary should only include the characters in the string. 

The test should be case-insensitive ("A" should be counted as "a").

The keys in the dictionary should be lowercase letters.

Only include letters in the dictionary.
"""

s = "Hello, World"
new_s = {}

# option 1

# for i in s.lower():
#     if i not in new_s:
#         new_s[i] = 1
#     else:
#         new_s[i] += 1
# print(new_s)

# option2

for char in s.lower():
    if char.isalpha():
        if char in new_s:
            new_s[char] += 1
        else:
            new_s[char] = 1

print(new_s)