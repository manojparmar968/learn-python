"""
Write a Python program that prints a triangular pattern made with letters (as shown below).

The first row should have one letter A (in uppercase). The second row should have two letters B. The third row should have three letters C and so on.

The number of rows is determined by the value of n, which is entered by the user.

The letters must be separated by a space.

Hints:
The chr() function converts a number to its corresponding character.

The ASCII code points for uppercase letters start at 65 for "A".
"""

n = 3

for i in range(0,n):
    print(chr(65 + i) * (i + 1))