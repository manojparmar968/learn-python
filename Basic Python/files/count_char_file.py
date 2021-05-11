"""
Write a Python program that counts the number of characters in a file.

Count all the characters in the file, including commas and quotes.

Do not count spaces and remove \n (new line) characters.

Hints:
You can use the .strip() method to remove the \n characters from each line.

You can also use the .replace() method to replace spaces by empty strings.

"""

file_path = '/home/developer/Desktop/project/python/udemy/files/text.txt'

char_count = 0

with open(file_path) as file:
    for line in file:
        char_count += len(line.replace(" ", "").strip("\n"))
print(char_count)