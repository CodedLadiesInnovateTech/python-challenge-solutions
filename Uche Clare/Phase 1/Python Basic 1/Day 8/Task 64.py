#program to get file creation and modification date/times.
import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("Anaconda")))
print("Created: %s" % time.ctime(os.path.getctime("Anaconda")))