#program to create a list reflecting the modified run-length 
# encoding from a given list of integers or a given list of characters.
from itertools import groupby
def modified_encode(alist):
        def ctr_ele(el):
            if len(el)>1: return [len(el), el[0]]
            else: return el[0]
        return [ctr_ele(list(group)) for key, group in groupby(alist)]

n_list = [1,1,2,3,4,4,5, 1]
print("Original list:") 
print(n_list)
print("\nList reflecting the modified run-length encoding from the said list:")
print(modified_encode(n_list))

n_list = 'aabcddddadnss'
print("\nOriginal String:") 
print(n_list)
print("\nList reflecting the modified run-length encoding from the said string:")
print(modified_encode(n_list))