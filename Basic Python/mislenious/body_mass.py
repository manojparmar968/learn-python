"""
Write a Python program that calculates body mass index.

The formula to calculate body mass index is BMI = kg/m2 where kg is a person’s weight in kilograms and m2 is their height in meters squared.

The user should be able to enter his or her height in centimeters and weight in kilograms.

You may assume that the height and weight entered will be positive integers.

The program must print a message with the value of the Body Mass Index (BMI) rounded to two decimals and the category:

Underweight = less than 18.5

Normal = from 18.5 to 24.9

Overweight = from 25 to 29.9

Obesity = 30 or greater

 Hints:
The formula uses meters squared but the user input will be in centimeters. 
You will need to convert the input to the appropriate units.
"""

print("Welcome to the Body Mass Index Calculator")

height = float(input("Please enter your height (cm): "))
weight = float(input("now enter your weight (kg): "))

height_meters = height / 100

BMI = round(weight / (height_meters ** 2), 2)

print(f"BMI: {BMI}")
print("You result is:", end=" ")

if BMI < 18.5:
    print("UnderWeight")
elif (BMI == 18.5) or (BMI <= 24.9):
    print("Normal")
elif 25 <= BMI <= 29.9:
    print("Overweight")
else:
    print("Obesity")