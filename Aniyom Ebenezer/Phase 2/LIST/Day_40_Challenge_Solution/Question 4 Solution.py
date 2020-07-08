"""
Write a Python program to print the numbers of specified list after removing even numbers from it.
"""
numbers = [1, 2, 4, 3, 5, 4, 5, 7, 89, 32, 40]
specified_list =[x for (i,x) in enumerate(numbers) if x % 2 != 0]
print(specified_list)