"""
Write a Python program that finds and prints the longest word in a text file.

For this challenge, you may assume that the file only contains one word per line.
"""

file_path = '/home/developer/Desktop/project/python/udemy/files/words.txt'

longest_word = ""

with open(file_path) as file:
    for word in file:
        if len(word) > len(longest_word):
            longest_word = word
print(longest_word)