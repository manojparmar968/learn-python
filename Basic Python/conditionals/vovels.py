"""
Write a Python program that prints a descriptive message indicating if each character in a string is a vowel or a consonant. For example: "<char> is a <consonant | vowel>"

If the character is a special character, number, or symbol, print "<char> is not a letter".

If the string is empty, print "Empty String".

Hints:
You should also check spaces in the string and indicate that a space is not a letter.

You can convert the string to lowercase before making the comparisons.

"""

s = "Score: 36"

if not s:
    print("Empty String")
else:
    for char in s.lower():
        if char in ("a","e","i","o","u"):
            print(f"{char} is a vowel")
        elif not char.isalpha():
            print(f"{char} is not a letter")
        else:
            print(f"{char} is a consonant")