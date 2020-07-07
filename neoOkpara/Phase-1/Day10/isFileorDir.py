import os

path = "C:/Users/P7957/Desktop/python-challenges-solution/neoOkpara/Phase-1/Day10/isFileorDir.py"

if os.path.isdir(path):
    print("\nIt is a directory")
elif os.path.isfile(path):
    print("\nIt is a normal file")
else:
    print("It is a special file (socket, FIFO, device file)")
