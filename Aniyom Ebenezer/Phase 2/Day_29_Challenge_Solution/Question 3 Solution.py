"""
Write a Python program to get a string made of the first 2 and last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string 
Sample String: 'codedladies'
Expected Result: 'coes'
Sample String: 'co'
Expected Result: 'coco'
Sample String: 'c'
Expected Result: Empty string
"""
def made_string(str1):
    if len(str1) < 2:
        return " "
    else:
        return str1[0:2] + str1[-2:]
print(made_string("codedladies"))
print(made_string("co"))
print(made_string("c"))