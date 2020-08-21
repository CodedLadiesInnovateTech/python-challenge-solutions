'''
Write a Python program to get the size of a file.
'''

import os

failu = os.path.getsize(os.getcwd())

print("The size of the current file in the directory is:", failu)