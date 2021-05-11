"""
Write a Python program that copies the content of a file to another file.

If the new file doesn't exist, the program should create it.
"""

file_path = '/home/developer/Desktop/project/python/udemy/files/text.txt'
copy_path = '/home/developer/Desktop/project/python/udemy/files/text_copy.txt'

with open(file_path) as file, open(copy_path, "w") as copy:
    for line in file:
        copy.write(line)
