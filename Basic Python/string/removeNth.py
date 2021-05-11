"""
Write a Python program that prints the string s without the character at index n.

If the index n is out of range, print the string s intact.

If the string s is empty, print the string s intact.
"""
s = "manoj"
s1= ""
n = 1 # n is index

# option 1

if (len(s) == 0) or (n >= len(s)):
    print(s)
else:
    new_s = ""
    for i in range(len(s)):
        if i != n:
            new_s += s[i]
    print(new_s)