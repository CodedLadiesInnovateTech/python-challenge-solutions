'''
Write a Python program to check whether a file path is a file or a directory.
'''

import os, inspect

fPath = os.path.os.getcwd
    if os.path.isdir(fPath):
        print("It is a directory.")
    elif os.path.isfile(fPath):
        print("It is a file.")
    else:
        print("It is a neither a file nor a directory.")
# print(inspect.getfile(inspect.currentframe()))