#Write a Python program to make file lists from current directory using a wildcard.
import glob
file_lists = glob.glob('*')
print(file_lists)