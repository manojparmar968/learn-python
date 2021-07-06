"""
Write a Python program that prints the elements of a list on the same line.

The elements should be separated only by a space (not by a comma).

The output should not include the opening and closing square brackets [ ].
"""

# s = ["a","b","c"]
s = [3,4,5,6]

# option 1

new_s = ""

# for i in s:
#     new_s += "".join(i) + " "
# new_s.rstrip()
# print(new_s,end=" ")

# option 2

for i in s:
    print(i, end=" ")

# option 3 

print(*s, end=" ")