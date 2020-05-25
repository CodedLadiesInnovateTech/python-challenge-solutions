#program to get the path and name of the file that is currently executing
import os, sys
print(os.path.dirname(os.path.realpath(sys.argv[0])))