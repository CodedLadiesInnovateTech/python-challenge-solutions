'''10. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.'''


lst1 = [100, 115, 5505, 600, 457, 675, 1555, 754, 8909, 200, 6084]
lst2 = list(filter(lambda i: (i%15), lst1))
print(lst2)