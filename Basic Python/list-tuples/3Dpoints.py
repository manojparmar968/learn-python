"""
Write a Python program that calculates the distance between two 3D points.

The points are represented by two lists with three elements. 
The first element is the x-coordinate. The second element is the y-coordinate. 
The third element is the z-coordinate.
"""

pointA = [3,4,5]
pointB = [1,3,5]

# option 1

# distance = (
#     (pointA[0] - pointB[0]) ** 2 + 
#     (pointA[1] - pointB[1]) ** 2 + 
#     (pointA[2] - pointB[2]) ** 2) ** (1 / 2)
# print(distance)

# option 2
import math

sum = ((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2 + (pointA[2] - pointB[2]) ** 2)
distance = math.sqrt(sum)
print(distance)