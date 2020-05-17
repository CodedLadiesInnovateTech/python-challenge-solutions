from math import sqrt
def distance(x_1, y_1, x_2, y_2):
    dist = sqrt((x_1 - x_2) ** 2 + (y_1 - y_2)** 2)
    return print(f"the distance between point {x_1,y_1} and point {x_2,y_2} is :", dist)
distance(3,5,2,1)
