import math


def calc_distance(p1=(), p2=()):
    x_gradient = (p2[0] - p1[0])**2
    y_gradient = (p2[1] - p1[1])**2
    distance = math.sqrt(y_gradient + x_gradient)
    print (round(distance, 2))


calc_distance((1, 2), (3, 9))

point_1 = [4, 0]
point_2 = [6, 6]
calc_distance(point_1, point_2)

