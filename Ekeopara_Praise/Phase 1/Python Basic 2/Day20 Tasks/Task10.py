'''10. Write a Python program to check whether a point (x,y) is in a triangle or not. There is a triangle formed by three points.
Input:
x1,y1,x2,y2,x3,y3,xp,yp separated by a single space.
Input three coordinate of the circle:
9 3 6 8 3 6
Radius of the said circle:
3.358
Central coordinate (x, y) of the circle:
6.071 4.643'''

print("Input x1,y1,x2,y2,x3,y3,xp,yp:")
x1,y1,x2,y2,x3,y3,xp,yp = map(float, input().split())
c1 = (x2-x1)*(yp-y1)-(y2-y1)*(xp-x1)
c2 = (x3-x2)*(yp-y2)-(y3-y2)*(xp-x2)
c3 = (x1-x3)*(yp-y3)-(y1-y3)*(xp-x3)
if (c1<0 and c2<0 and c3<0) or (c1>0 and c2>0 and c3>0):
    print("The point is in the triangle.")
else:
    print("The point is outside the triangle.")

#Reference: w3reource