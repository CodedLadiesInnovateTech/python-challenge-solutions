# program to check whether a file path is a file or a directory.
import os  
path="C:/Users/pc/Desktop/Python Task Solutions/Uche Clare/Phase 1/Python Basic 1/Day 10"  
if os.path.isdir(path):  
    print("It\'s a directory")  
else:
    print("It\'s a normal file")  
