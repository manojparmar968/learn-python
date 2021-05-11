"""
Write a Python program that writes the elements of a list to the file denoted by the variable file.

Each element should be written on a separate line.

The file should be new or its existing content must be replaced by this new content.

Hints:
You will need to add a \n (new line) character to write the elements on separate lines.
"""

file_path = '/home/developer/Desktop/project/python/udemy/files/list.txt'

my_list = [1, 2, 3, 4, 5]

with open(file_path, "w") as file:
    for elem in my_list:
        file.write(str(elem) + "\n")