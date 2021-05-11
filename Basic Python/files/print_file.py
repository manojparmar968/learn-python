"""
Write a Python program that reads a text file and prints the first n lines of the file.

The value of n should be entered by the user.

If the value of n is greater than the total number of lines in the file, print

"Please enter a value for n. The file has <num_lines> lines".

Hints:
It is recommended to use a with statement to work with files in Python.

The readlines() method returns the lines in a file as a list.

Notice that the output doesn't have a space in between each line. 
You can use the .strip() method to remove the \n character from each line, 
which will add an extra blank line between each line in the output.
"""

file_path = '/home/developer/Desktop/project/python/udemy/files/basic_file.txt'

n = int(input("How many lines would you like to read?: "))

with open(file_path) as file:
    lines = file.readlines()
    num_lines = len(lines)

    if num_lines < n:
        print(f"Please enter value. The file has {num_lines} lines")
    else:
        for i in range(n):
            print(lines[i].strip("\n"))