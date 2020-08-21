from math import sqrt
def distance(x1,x2,y1,y2):
    d=sqrt((x2-x1)**2 + (y2-y1)**2)
    return d

print(distance(3,2,5,1))


