'''1. Write a Python program to split a variable length string into variables.'''
mylist = [1, 2, 3, 4, 5]
a, b, c, d, e =(mylist + [None] * 5)[:5]
print(a, b, c, d, e)

