#write a Python program to get the actual module object for a given object.
import inspect
import math
print(inspect.getmodule(math.sqrt))