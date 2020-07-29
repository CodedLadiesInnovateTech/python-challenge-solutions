'''
Write a Python program to unzip a list of tuples into individual lists.
'''
l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))