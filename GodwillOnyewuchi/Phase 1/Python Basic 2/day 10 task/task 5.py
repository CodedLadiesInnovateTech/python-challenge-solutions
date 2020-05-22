# Python program to check whether a file path is a file or a directory

import os
path="task 7.py"
if os.path.isdir(path):
    print("It is a directory")
elif os.path.isfile(path):
    print("It is a normal file")
else:
    print("It is a special file (socket, FIFO, device file)" )