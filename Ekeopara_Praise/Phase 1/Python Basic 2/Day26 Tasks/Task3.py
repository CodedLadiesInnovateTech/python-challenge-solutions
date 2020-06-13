'''3. Write a Python program to find the middle character(s) of a given string. If the length of the string is odd return the middle 
character and return the middle two characters if the string length is even.
Sample Output:
th
H
av'''
def middle_char(txt):
   return txt[(len(txt)-1)//2:(len(txt)+2)//2]
print(middle_char("Python"))
print(middle_char("PHP"))
print(middle_char("Java"))

#Reference: w3resource