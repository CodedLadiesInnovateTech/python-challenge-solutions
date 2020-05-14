import math


def sphere_volume(radius):
    pie = math.pi
    volume = (4 / 3) * pie * math.pow(radius, 3)
    return volume


print (sphere_volume(2))
