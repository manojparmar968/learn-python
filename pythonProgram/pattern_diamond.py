"""
     *
    ***
   *****
  *******
   *****
    ***
     *
"""

h = 7

if h%2 == 0:
    print("Enter the height odd number")
else:
    middle_row = (h+2)//2
    for i in range(middle_row):
        print(" " * (middle_row-i), "*" * (i*2+1))

    for i in range(middle_row-2,-1,-1):
        print(" " * (middle_row-i), "*" * (i*2+1))