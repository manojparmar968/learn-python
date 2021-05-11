"""
Write a Python program that prints the corresponding season based on the value of the variable season_num.

The possible values of season_num are: 1 for Spring, 2 for Summer, 3 for Fall, 4 for Winter.

If the value of season_num is neither one of these values, print "Please enter a valid number".
"""

num = 5

if num == 1:
    print("Spring")
elif num == 2:
    print("Summer")
elif num == 3:
    print("Fall")
elif num == 4:
    print("Wintter")
else:
    print("Please enter a valid number")