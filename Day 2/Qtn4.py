"""
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
    Sample Output :
        r = 1.1
        Area = 3.8013271108436504
    Tools: input function
"""

from math import pi

r = float(input("Enter radius ="))

area = pi * r ** 2

print("Area =", area)