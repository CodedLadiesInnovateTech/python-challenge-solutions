'''9. Write a Python program to display a floating number in specified numbers.'''

lst1 = [1, 2.5, 3, 4.5, 4, 5.5]

New_list = list(filter(lambda i: type(i) == float, lst1))
print(New_list)