#program to check whether a file exists.
import os.path

def main(filename, ext):
    return os.path.isfile(filename + '.' + ext)
print(main('C:/Users/pc/Desktop/Python Task Solutions/Uche Clare/Phase 1/Python Basic 1/Day-5/Task 31', 'py' ))
    