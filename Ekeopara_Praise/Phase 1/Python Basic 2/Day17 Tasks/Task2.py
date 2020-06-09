'''2. Write a Python program to create all possible permutations from a given collection of distinct numbers'''

from itertools import permutations
lst = [4, 6, 7]
perm = permutations(lst)
for i in list(perm):
    print(i)
