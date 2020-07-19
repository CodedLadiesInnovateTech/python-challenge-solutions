"""
Write a Python program to flatten a shallow list. 
"""
import itertools
original_list = [[2,3,4],  [1,4,7], [9], [7,9,0]]
new_merged_list = list(itertools.chain(*original_list))
print(new_merged_list)