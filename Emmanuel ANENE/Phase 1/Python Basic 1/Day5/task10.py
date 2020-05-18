from math import *

x1 = int(input("Enter x1 number: "))
x2 = int(input("Enter x2 number: "))
y1 = int(input("Enter y1 number: "))
y2 = int(input("Enter y2 number: "))


def dist(x1, y1, x2, y2):
    return sqrt(pow(x2 - x1, 2) + pow (y2 -y1, 2) * 1.0)

print(dist(x1, y2, x2, y2))