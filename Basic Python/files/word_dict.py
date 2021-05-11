"""
Write a Python program that creates and prints a frequency dictionary of the words found in a text file.

The keys of the dictionary should be the words in the file.

The values should be their frequencies.

You may assume that each line of the file only contains one word.

Hints:
If you read the file line by line, 
you will need to use the .strip() method to remove the \n character from the end of each line.
"""

file_path = '/home/developer/Desktop/project/python/udemy/files/words.txt'

dict_word = {}

with open(file_path) as file:
    for i in file:
        i = i.strip("\n")
        if i not in dict_word:
            dict_word[i] = 1
        else:
            dict_word[i] += 1
print(dict_word)