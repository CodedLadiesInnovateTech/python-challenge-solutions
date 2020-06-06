#Python program to get the size of an object in bytes
import sys
Object = input("Enter any object: ")

print(f'The size of the object {Object} is {sys.getsizeof(Object)} bytes')
