'''4. Write a Python program to filter the positive numbers from a list.'''

lst = [1, -3, 4, -56, 7, 3, -8, -5, 2, 4, 9]
New_list = list(filter(lambda x: x > 0, lst))
print(New_list)
