#program to add two objects if both objects are an integer type.
import math
def sum(c, d):
    if not (isinstance(c, int) and isinstance(d, int)):
         raise TypeError("Inputs must be integers")
    return c + d

print(sum(10, 20))
print(sum(6.4, 14))