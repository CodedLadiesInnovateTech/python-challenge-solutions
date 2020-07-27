'''10. Write a Python program to capitalize first and last letters of each word of a given string. '''

teststring = "python"
f = teststring[0]
l = teststring[-1]
print(f.upper() + teststring[1:-1] + l.upper())