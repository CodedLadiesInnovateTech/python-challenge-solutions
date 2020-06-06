# Python program to check whether a string is numeric

String = input("Enter any value: ")

if int(String) + 2 == int(String) + 4 -2:
    print(f'Input is numeric')
else:
    print(f'Input is not numeric')