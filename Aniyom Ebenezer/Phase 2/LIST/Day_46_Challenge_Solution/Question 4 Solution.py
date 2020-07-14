"""
Write a Python program to pack consecutive duplicates of a given list elemnts into sublists.
"""
from itertools import groupby
def pack_consecutive_list(n_list):
    return (list(group) for group, key in groupby(n_list))
n_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 4, 4]
print("Original List: ")
print(n_list)
print("\nPacked Consecutive list: ")
print(pack_consecutive_list(n_list))