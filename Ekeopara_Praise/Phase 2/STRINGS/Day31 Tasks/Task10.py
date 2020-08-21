'''10. Write a Python program to print the following floating numbers upto 2 decimal places. '''

def two_decimalplaces(floatnumber):
    num = round(floatnumber, 2)
    return num
print(two_decimalplaces(1234.567))