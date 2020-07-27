'''9. Write a Python program to list all files in a directory in Python.'''

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('C:/Users/Sir_Praise/Documents/PYTHON LEARNING') if isfile(join('C:/Users/Sir_Praise/Documents/PYTHON LEARNING', f))]
print(files_list)
