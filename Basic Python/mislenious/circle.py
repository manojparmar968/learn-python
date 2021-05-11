"""
Write a Python program that finds the area of a circle from the value of the diameter d.

The value of d should be provided by the user.

The area of a circle is equal to pi*(radius)^2. The radius is the value of the diameter divided by 2.

Round the value of the area to two decimal places.

You may assume that the value of the diameter will be non-negative integer.

Hints:
The math module has a pi constant that you can use in your program. To import it, write import math at the top of your program and then math.pi where you want to use pi.

The round() function rounds a value to the specified number of decimal places.

If the area is 0, you may present it as 0.0
"""

import math

diameter = int(input("Please enter the diameter: "))
radius = diameter/2

area = round(math.pi * (radius**2), 2)
print(f"The area of a circle with diameter {diameter} is {area}")