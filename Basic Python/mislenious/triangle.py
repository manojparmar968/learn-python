"""
Write a Python program that computes the area of a triangle from its base and height.

The program should print the area of the triangle rounded to two decimal places (if necessary).

The values of base and height should be entered by the user.

The area of a triangle is found with this formula: (base*height)/2

If either one of the values is invalid, the program should print

"Please enter valid values for base and height".
"""

base = int(input("Enter the base: "))
height = int(input("Enter the height: "))

if base > 0 and height > 0:
    area = round((base * height) / 2, 2)
    print(f"The area of a triangle with base {base} and height {height} is: {area}")
else:
    print("Please enter valid values for base and height")