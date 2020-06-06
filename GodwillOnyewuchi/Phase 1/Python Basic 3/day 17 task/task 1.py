# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other

List = [1, 2, 3, 5, 4, 6, 5]

if len(List) == len(set(List)):
    print(f'All numbers in the sequence are different')
else:
    print(f'Not all the numbers in the sequence are different')


