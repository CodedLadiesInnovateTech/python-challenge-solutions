'''
Write a Python program to calculate the hypotenuse of a right angled triangle
'''

import math as m

b = int(input("Enter the base of the triangle: "))
c = int(input("Enter the height of the triangle: "))

a = round(m.sqrt(m.pow(b, 2) + m.pow(c, 2)), 2)

print("The hypotenuse of the right angled triangle is => {}".format(a))
