'''9. Write a Python program to get the size of an object in bytes.'''
import sys
def object_size(obj):
    return f"The size of {obj} is {sys.getsizeof(obj)} bytes"
print(object_size("love"))
print(object_size(457))

