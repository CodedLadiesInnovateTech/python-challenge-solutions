
#Write a Python program to get the command-line arguments (name of the script,
# the number of arguments, arguments) passed to a script
import sys

print(f'This is the name/path of the script: {sys.argv[0]}')
print(f'Number of arguments: {len(sys.argv)}')
print(f'Argument List: {str(sys.argv)}')
