'''1. Write a Python program to check whether a file exists.'''

import os.path
open("later.txt", 'w')
print(os.path.isfile('later.txt'))