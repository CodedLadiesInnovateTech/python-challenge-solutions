#2. Write a Python program to get the least common multiple (LCM) of two positive integers.

import math

a = int(input("Enter a positive integer:"))
b = int(input("Enter another positive integer:"))

if a > b:
    greater = a

else:
    greater = b

while(True):
    if((greater % a ==0) and (greater % b ==0)):
        lcm = greater
        break
    greater += 1

print("The LCM of {} and {} is {}".format(a,b,lcm))


