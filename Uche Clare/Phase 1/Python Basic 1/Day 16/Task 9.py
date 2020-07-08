#Write a Python function that takes a positive integer and returns the sum 
# of the cube of all the positive integers smaller than the specified number.
import math

x = int(input('Postive integer: '))
sum = 0
for i in  range(1, x):
    sum = sum + math.pow(i, 3)
print(sum)
