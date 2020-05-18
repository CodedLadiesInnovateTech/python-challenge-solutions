'''10. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).'''
from math import sqrt
x1, x2 = 4, 8
y1, y2 = 6, 12
dist = ((x2-x1)**2) + ((y2 - y1)**2)
dist = sqrt(dist)

print(f"The Distance between the points is: {dist}")
