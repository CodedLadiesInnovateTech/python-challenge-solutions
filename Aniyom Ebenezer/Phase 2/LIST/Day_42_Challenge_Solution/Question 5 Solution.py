"""
Write a Python program to create a list by concatenating list which range goes from 1 to n
"""
list1 = ['p','q']
n = 5
list2 = ['{}{}'.format(x, y ) for y in range(1, n+1) for x in list1]
print(list2)