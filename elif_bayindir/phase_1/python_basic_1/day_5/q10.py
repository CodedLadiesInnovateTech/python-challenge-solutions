# Question 10
# Distance between 2 points

from math import sqrt

x1 = float(input("Enter first points' x: "))
y1 = float(input("Enter first points' y: "))
x2 = float(input("Enter second points' x: "))
y2 = float(input("Enter second points' y: "))

distance = sqrt(((x1-x2)**2)+((y1-y2)**2))
print("Distance between 2 points:", distance)
