'''4. Write a Python program to print the numbers of a specified list after removing even numbers from it. '''

lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = list(filter(lambda x: x%2 != 0, lst1))
print(lst2)