#Write a Python program to check if a number is positive, negative or zero.
num = int(input('Enter number:'))
if num == 0:
    print('The number is zero.')
elif num <= 0:
    print('The number is a negative value')
else:
    print('The number is a postive value')