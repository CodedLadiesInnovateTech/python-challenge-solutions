# Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

if num1 % num2== 0:
    print(f'{num1} is divisible by {num2}')
else:
    print(f'{num1} is not divisible by {num2}')