#program to compute the distance between the points (x1, y1) and (x2, y2).
import math
x1=int(input('Enter x1: '))
x2=int(input('Enter x2: '))
y1=int(input('Enter y1: '))
y2=int(input('Enter y2: '))
x =x2-x1
y=y2 - y1
z= math.sqrt(math.pow(x, 2) + math.pow(y, 2))
print(z)