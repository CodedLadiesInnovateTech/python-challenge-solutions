'''
Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
'''

import sys

length = len(sys.argv)

print("Total arguments passed: ", length)
print("\nName of Python script: ", sys.argv[0])
print("\nThe Arguments passed: ", end=" ")

for i in range(1, length):
    print(sys.argv[i], end=" ")
