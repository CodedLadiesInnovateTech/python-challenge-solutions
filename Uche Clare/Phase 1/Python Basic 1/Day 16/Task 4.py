#Write a Python program to check whether variable is of integer or string.
n = input('Enter: ')
try:
    print(int(n))
    print(f'{n} is an integer')
except ValueError:
    print(f'{n} is a string')