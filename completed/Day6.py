"""
Day 6 - Calculate the area of a circle.
Write a program that takes radius of the circle and outputs the area of the circle to 2 decimal digits
"""

import math

radius = int(input("Enter Radius of Circle: "))
print(f"The area of a circle is {2 * math.pi * radius:.2f}")