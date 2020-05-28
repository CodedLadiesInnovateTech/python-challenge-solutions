#Write a Python program to create a copy of its own source code
s='s=%r'
print(s%%s)
print(s%s)