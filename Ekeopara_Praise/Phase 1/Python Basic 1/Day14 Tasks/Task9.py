'''9. Write a Python program to add leading zeroes to a string.'''

string = '6567.45'
new_string = string.ljust(9, '0')
print(new_string)