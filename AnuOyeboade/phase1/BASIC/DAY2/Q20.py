"""
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
    Tools: input function, slicing
"""
string = str(input("Enter a word"))
a = int(input("Enter the amount of times word should be repeated"))
if a>0:
    print(a*string)
else:
    print("enter a positive number")

