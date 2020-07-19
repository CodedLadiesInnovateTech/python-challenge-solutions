'''8. Write a Python program to check whether lowercase letters exist in a string.'''
def checklowercase(string):
    response = any((l.islower() for l in string))
    return response
print(checklowercase('Strong'))
print(checklowercase('light'))
