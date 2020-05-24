import os.path
import time

# os.path.getmtime(path) and os.path.getctime(path) returns a float which is then converted to a time object using
# time.ctime

path = "C:/Users/P7957/Desktop/python-challenges-solution/neoOkpara/Phase-1/Day8/task4.py"
print("Last modified: %s" % time.ctime(os.path.getmtime(path)))
print("Created: %s" % time.ctime(os.path.getctime(path)))


