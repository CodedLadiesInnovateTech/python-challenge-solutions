#program to compute the distance between the points (x1, y1) and (x2, y2)
#d= sqrt(x2-x1)**2+(y2-y1)**2
import math
p1 = [8, 4]
p2 = [10, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)