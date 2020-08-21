'''
Write a Python program to get file creation and modification date/times.
'''

import os

# print(os.path.getctime(os.path.getmtime()))
print("The current modification time of the cureent directory is", os.stat(os.getcwd()))