
# Python program to prove that two string variables of same value point same memory location

String1 = 'word'
String2 = 'Word'

print(f'Memory location of String1 = {hex(id(String1))}')
print(f'Memory location of String2 = {hex(id(String2))}')

