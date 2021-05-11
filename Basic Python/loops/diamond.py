"""
Write a Python program that prints a diamond made with asterisks where the diamond's height (number of rows) is determined by the value of the variable height

You can (optionally) ask the user to enter the value of height.

This value can only have an odd number of rows, so you should print a descriptive message if the user enters an even value.

Hints:
You may need to use multiple loops to print different parts of the pattern.
"""

height = 7

if height % 2 == 0:
    print("Please enter a odd value for height .")
else:
    middle_row = (height + 2) // 2

    for i in range(middle_row):
        print(" " * (middle_row - i), "*" * (i*2 + 1))

    for i in range(middle_row-2, -1, -1):
        print(" " * (middle_row - i), "*" * (i*2 + 1))