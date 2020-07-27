#program to list all files in a directory in Python.
from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/Desktop') if isfile(join('/Desktop', f))]
print(files_list)