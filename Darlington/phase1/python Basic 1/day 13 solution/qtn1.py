#program to make file lists from current directory using a wildcard.
import glob
file_list = glob.glob('*.*')
print(file_list)