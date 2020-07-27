# write a Python program to check whether variable is of integer or string

var = "hello"

try:
    print(int(var))
    print(f'{var} is an integer')
except ValueError:
    print(f'{var} is a string')