# Write a Python program to determine whether variable is defined or not.


try:
    print(a)
    print("variable is defined")
except NameError:
    print("Variable not defined")