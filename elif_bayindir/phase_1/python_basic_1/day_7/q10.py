# Question 10
# Hypotenuse of a right angled triangle.

from math import sqrt

edge1 = float(input("Enter 1st edge: "))
edge2 = float(input("Enter 2nd edge: "))
hyp = sqrt((edge1 ** 2 + edge2 ** 2))
print("Hypotenuse of a right angled triangle:", hyp)

