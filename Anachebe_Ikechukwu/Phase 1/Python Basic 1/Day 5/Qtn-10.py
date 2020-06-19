#10. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math

x1 = int(input('enter x1 axis:'))
y1 = int(input('enter y1 axis:'))
x2 = int(input('enter x2 axis:'))
y2 = int(input('enter y2 axis:'))

dist = math.sqrt(((x2 - x1)** 2) + ((y2 - y1)** 2))

print(dist, 'cm')