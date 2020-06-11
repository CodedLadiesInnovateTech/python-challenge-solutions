"""
There are two circles C1 with radius r1, central coordinate (x1, y1) and C2 with radius r2 and central coordinate(x2,y2) 
Write a Python program to test the followings
"C2 is in C1" if C2 is in C1
"C1 is in C2" if C1 is in C2
"Circumference of C1 and C2 intersect" if circumference of C1 and C2 intersect and
"C1 and C2 don not overlap " if C1 and c2 do not overlap
"""
import math
print("Input x1, y1, x2, y2, r1, r2: ")
x1, y1, x2, y2, r1, r2 = [float(i) for i in input().split()]
d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
if d < r1-r2:
    print("C2 is in C1")
elif d < r2-r1:
    print("C1 is in C2")
elif d > r1 + r2:
    print("Circumference of C1 and C2 intersect.")
else:
    print("C1 and C2 don not overlap")