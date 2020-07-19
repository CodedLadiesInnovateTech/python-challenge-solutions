#program to find the middle character(s) of a given string.
def middle_char(txt):
   return txt[(len(txt)-1)//2:(len(txt)+2)//2]
print(middle_char("Python"))
print(middle_char("PHP"))
print(middle_char("Java"))