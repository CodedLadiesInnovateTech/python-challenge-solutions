#Write a Python program to find files and skip directories of a given directory.
import os
for i in os.listdir('c:/Users/HP/Desktop/Python Solutions/Uche Clare/Phase 1/Python Basic 1'):
    if os.path.isfile(os.path.join(__file__)):
        print(i)