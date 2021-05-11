"""
Write a Python program that prints all the letters in the alphabet using a loop (one letter per line).

The program should print the letters in uppercase.

Hints:
The chr() function converts a Unicode code point into its corresponding character.

Uppercase letters start at the code 65 and end at code 90.
"""

for i in range(65, 91):
    print(chr(i))