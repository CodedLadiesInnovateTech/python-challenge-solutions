'''
Write a Python program to remove an item from a set if it is present in the set.
'''
num_set = set([0, 1, 2, 3, 4, 5])
num_set.discard(4)
print(num_set)