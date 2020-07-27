#Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder. 
import math
length = 13
width = 12
rad = 15
area = length * width                               #Area of a rectangle 
volume = 4/3 * math.pow(rad, 3)                             #Volume of a cylinder
print('Area of a rectangle = ',area,u"cm\u00b2")
print('Volume of a cylinder = ',volume, u'cm\u00b3')