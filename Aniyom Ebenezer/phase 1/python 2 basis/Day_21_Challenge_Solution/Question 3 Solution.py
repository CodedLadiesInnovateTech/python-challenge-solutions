"""
Write a Python program to test whether two lines PQ and RS are parallel. The points are:
P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4).
"""
print("Input x1, y1, x2, y2, x3, y3, x4, y4: ")
x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
if abs((x2 - x1)*(y4 - y3) - (x4 - x3)*(y2 - y1)) < 1e-10:
    print("PQ and RS are parallel")
else:
    print("PQ and Rs are not parallel")