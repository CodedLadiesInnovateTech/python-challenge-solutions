import math

point1 = (1, 1)
point2 = (4, 5)
x_total = point2[0] - point1[0]
y_total = point2[1] - point1[1]

total = math.sqrt((math.pow(x_total, 2)) + (math.pow(y_total, 2)))
print(total)