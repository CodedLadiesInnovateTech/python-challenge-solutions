'''6. Write a Python program to divide a path on the extension separator.'''

import os 
file = r'C:\Users\Sir_Praise\Documents\PYTHON LEARNING.py'
path_div = os.path.splitext(file)
print()
print(f"The root path of {file} is:\n{path_div[0]}")
print()
print(f"The extension path of {file} is:\n{path_div[1]}")


