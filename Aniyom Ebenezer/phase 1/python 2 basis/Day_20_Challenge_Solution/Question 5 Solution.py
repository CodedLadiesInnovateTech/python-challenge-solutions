"""
Write a Python program which solves the equation:
ax+by=c
dx+ey=f
print the values of x, y where a,b,c,d,e and f are given.
"""
a, b, c, d, e, f = map(float, input("Input the values of a,b,c,d,e and f: ").split())
n = a*e - b*d
print("Values of x and y:")
if n != 0:
    x = (c*e - b*f)/ n
    y = (a*f - c*d) / n
    print("{:.3f} {:.3f}".format(x+0, y+0))