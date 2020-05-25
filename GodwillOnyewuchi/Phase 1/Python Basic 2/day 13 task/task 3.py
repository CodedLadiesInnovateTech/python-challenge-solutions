# Python program to input a number, if it is not a number generate an error message

try:
    Input = int(input("Please enter an integer: "))
    print(f'Input = {Input}')
except ValueError:
    print("Input is not a number")
