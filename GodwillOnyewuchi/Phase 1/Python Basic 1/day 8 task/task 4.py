import os.path
import time

print("Last modified: %s" % time.ctime(os.path.getmtime("task 1.py"))) 
print("Created: %s" % time.ctime(os.path.getctime("task 1.py")))
