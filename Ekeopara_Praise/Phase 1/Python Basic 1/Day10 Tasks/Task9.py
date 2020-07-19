'''9. Write a Python program to perform an action if a condition is true.
Given a variable name, if the value is 1, display the string "First day of 
a Month!" and do nothing if the value is not equal.'''
import sys
var = int(input("Enter any number: "))
if var == 1:
    print("\"First day of a Month!\"")
else:
    sys.exit()