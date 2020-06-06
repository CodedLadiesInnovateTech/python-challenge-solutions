# Write a Python program to get the actual module object for a given object

from inspect import getmodule
from math import pow

print(getmodule(pow))

