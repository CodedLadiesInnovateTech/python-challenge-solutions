#program to check whether two given circles (given center (x,y) and radius) are intersecting.
#  Return true for intersecting otherwise false.
def is_circle_collision(circle1, circle2):
   x1, y1, r1 = circle1
   x2, y2, r2 = circle2
   distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
   return distance <= r1 + r2
print(is_circle_collision([1,2, 4], [1,2, 8]))
print(is_circle_collision([0,0, 2], [10,10, 5]))