"""
Write a Python program that reads a text file and saves its content line by line to a list called file_content.

The list should contain strings that represent each line of the text file.

The program should print the resulting list.

Hints:
It is recommended to use a with statement to work with files in Python.
"""

file_path = '/home/developer/Desktop/project/python/udemy/files/basic_file.txt'

file_content = []

with open(file_path) as file:
    for line in file:
        file_content.append(line)

print(file_content)