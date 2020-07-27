#program to sum of three given integers. However
import math
def sum_three(x, y, z):
    if x == y or y == z or x == z:
        sum_three = 0
    else:
        sum_three = x + y + z
    return sum_three

print(sum_three(7, 6, 7))
print(sum_three(9, 4, 4))
print(sum_three(5, 5, 5))
print(sum_three(12, 10, 3))
print(sum_three(5, 6, 6))