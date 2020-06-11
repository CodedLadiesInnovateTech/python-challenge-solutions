 
#5. Write a Python program to get the volume of a sphere with radius 6.
    #Tools: input function, math


from math import pi

radius = int(input("Enter Sphere Raduis:"))

r = radius

volume =((4/3)*pi)*(r**3)

print(volume)