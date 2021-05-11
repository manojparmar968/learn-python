"""
Write a Python program to count the number of repeated characters in the string s.

The program must print the total number of repeated characters and a message on the next line displaying the repeated characters separated by a space and sorted alphabetically.

If there are no repeated characters in the string, print 0 as the total count and None on the next line.
"""

s = "Corporation"
rep_count = 0
rep_chars = []

# option 1

# for char in s:
#     if (s.count(char) > 1) and (char not in rep_chars):
#         rep_count += 1
#         rep_chars.append(char)
# print(rep_count)

# if len(rep_chars) > 0:
#     for char in sorted(rep_chars):
#         print(char, end=" ")
# else:
#     print(None)

# option 2

# for char in s:
#     if (s.count(char) > 1) and (char not in rep_chars):
#         rep_count += 1
#         rep_chars.append(char)
# print(rep_count)

# if rep_chars:
#     print(*sorted(rep_chars), end=" ")
# else:
#     print(None)

# option 3

for char in s:
    if (s.count(char) > 1) and (char not in rep_chars):
        rep_chars.append(char)
print(len(rep_chars))

if rep_chars:
    print(*sorted(rep_chars), end=" ")
else:
    print(None)