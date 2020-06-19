#3. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

import math

x = int(input("Enter an integer:"))
y = int(input("Enter another integer:"))
z = int(input("Enter a third integer:"))

sum = x + y+ z

if((x == y) or (y == z) or (x == z)):
    sum = 0

print(sum)