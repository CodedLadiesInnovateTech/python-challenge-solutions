"""
Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
    Tools: math, input function
    """
import math
x = float(input("value for x is :"))
y = float(input("value for y is :"))
z = float(input("value for z is :"))
total = int(x+y+z)
if x==y==z:
    print(3*total)
else:
    print(total)