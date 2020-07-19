# Write a Python program to prove that two 
# string variables of same value point same memory location.

string_1 = 'Clare'
string_2 = 'Clare'
print('Memory location of string_1:', hex(id(string_1)))
print('Memory location of string_2:', hex(id(string_2)))