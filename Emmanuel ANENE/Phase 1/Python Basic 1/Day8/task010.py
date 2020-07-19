'''
Write a Python program to sort files by date.
'''

import glob, os

data = glob.glob("*.py")
data.sort(key=os.path.getctime)
print("\n".join(data))