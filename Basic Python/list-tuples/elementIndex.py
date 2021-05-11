"""
Write a Python program that prints the elements of a list followed their corresponding indices.

Each element and its index must be on the same line separated by a space.

If the list is empty, print "Empty List".
"""

# s = ["a","b","c"]
# s = [3,4,5,6]
s=[]

# option 1:

# if len(s) == 0:
#     print("Empty list")
# else:
#     for i in range(len(s)):
#         print(s[i],i)

# option 2

if not s:
    print("Empty list")
else:
    for i, elem in enumerate(s):
        print(elem,i)