"""
Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
"""
import math
x1 = float(input("x1 = "))
x2 = float(input("x2 = "))
y1 = float(input("y1 = "))
y2 = float(input("y2 = "))
x12 = float(x2-x1)**2
y12 = float(y2-y1)**2
d = math.sqrt(x12 + y12)
print(d)