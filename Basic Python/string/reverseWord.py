"""
Write a Python program that reverses the individual words in the string s and changes their capitalization. Uppercase letters should be printed in lowercase and vice versa.

Assume that the string only contains letters and spaces are used to separate words.
"""

s = "Hello World"

# option 1
# print(s.swapcase())

# option 2

words_list = s.split(" ")
new_s = ""

for word in words_list:
    reversed_word = "".join(reversed(word))
    # reversed_word = word[::-1]
    swapped_case = reversed_word.swapcase() # swapcase will change the character in upper to lower and lower to upper 
    new_s += swapped_case + " "
new_s.rstrip() #rstrip remove the space after the string
print(new_s)