'''
Write a Python program to check whether a file exists.
'''

import os as os

try:
    fileName = input("Enter a file name: ")
    get = open(fileName)
    get.close()
    print(get)
except:    
    print("File does not exist.")

print(os.__file__)