"""
Write a Python program that prints the last n lines of a text file in order.

The value of n should be provided by the user.

You may assume that n is a valid positive integer.
"""

file_path = '/home/developer/Desktop/project/python/udemy/files/basic_file.txt'

n = int(input("How many lines would you like to read?: "))

with open(file_path) as file:
    lines = file.readlines()
    num_lines = len(lines)

    if num_lines < n:
        print(f"Please enter value. The file has {num_lines} lines")
    else:
        for i in range(-n, 0):
            print(lines[i].strip("\n"))