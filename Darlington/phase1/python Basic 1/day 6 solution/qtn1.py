#program to check whether a file exists
import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))