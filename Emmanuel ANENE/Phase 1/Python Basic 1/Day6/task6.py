'''
Write a python program to get the path and name of the file that is currently executing.
'''

import os, inspect

print("The current path of the file is:", os.getcwd(), sep="\n\n", end="\f\n\f")

print("The curent name of the file is:", inspect.getfile(inspect.currentframe()), sep="\n\n", end="\n\n")