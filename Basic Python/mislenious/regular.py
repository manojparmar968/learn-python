"""
Write a Python program that checks if a string start with the string "My" and ends with the string "blue".

The program should also check if the string only contains alphanumeric characters.

For this program, you need to use a regular expression in Python. 
The built-in Python module re has very helpful functions to work with them, such as the search() function.

Hint:
This is an introduction to regular expressions in Python using the re module.
"""

import re 

regex = "^My[\w\s]+blue$"

string = input("Enter a string to check if match is found: ")

if re.search(regex, string):
    print("match")
else:
    print("No match")