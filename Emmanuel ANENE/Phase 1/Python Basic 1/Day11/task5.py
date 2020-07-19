'''
Write a Python program to check whether a string is numeric.
'''

inp1 = input("Enter the digit: ")

try:
    float(inp1)
    print("It is numeric.")
except(ValueError or TypeError):
    print("It is not numeric.")

