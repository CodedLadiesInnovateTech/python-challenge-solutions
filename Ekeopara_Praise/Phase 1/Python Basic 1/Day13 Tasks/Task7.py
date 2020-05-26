'''7. Write a Python program to prove that two string variables of same value point same memory location.'''

str1 = "Code"
str2 = "Code"

print("Memory Location of str1: ", hex(id(str1)))
print("Memory Location of str2: ", hex(id(str2)))

