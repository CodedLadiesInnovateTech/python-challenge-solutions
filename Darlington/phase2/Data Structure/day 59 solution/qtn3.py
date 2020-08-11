# program to get the array size of types unsigned integer and float.
from array import array
a = array("I", (12,25))
print(a.itemsize)
a = array("f", (12.236,36.36))
print(a.itemsize)