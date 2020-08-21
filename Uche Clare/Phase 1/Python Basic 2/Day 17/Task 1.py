#Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
num = [1, 2, 3, 3, 5]

if len(num) == len(set(num)):
    print(f'All numbers are different.')

else:
    print(f'Not all numbers are different.')