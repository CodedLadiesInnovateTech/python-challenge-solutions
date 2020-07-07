'''10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.'''

def change_string(strng):
    new_string = strng[-1] + strng[1:-1] + strng[0]
    return new_string
print(change_string("Praise"))
print(change_string("BooK"))
print(change_string("STOP"))
