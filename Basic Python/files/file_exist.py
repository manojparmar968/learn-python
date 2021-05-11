"""
Write a Python program that checks if a file exists in the specified path or not.

If it exists, print "The file <file_name> exists"

If it doesn't, print "The file <file_name> doesn't exist"

The file name could also be an absolute path to the file.

Hints:
The os.path module has an isfile() function that you can use to check if a file exists in a given path or not.
"""

import os.path

file_path = '/home/developer/Desktop/project/python/udemy/files/text.txt'
my_file = "text.txt"

if os.path.isfile(my_file):
    print(f"The file {my_file} exists")
else:
    print(f"The file {my_file} dosen't exists")