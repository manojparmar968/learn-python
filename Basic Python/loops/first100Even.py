"""
Write a Python program that prints the first 100 even numbers (from 2 to 200 inclusive).

Hints:
You can check if a number is even or odd with num % 2 == 0. If it's true, the number is even. Else, it's odd.

The range() function can take a third parameter to customize the step (difference) between the integers in the sequence.

"""

# option 1

for i in range(2, 201, 2):
    print(i)

# option 2

for i in range(1, 201):
    if i%2 == 0:
        print(i)