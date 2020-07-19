"""
Write a Python program to generate all sublists in a list.
"""
from itertools import combinations 
def sub_lists(list1):
    subs = []
    for i in range(0, len(list1)+1):
        temp = [list(x) for x in combinations(list1, i)]
        if len(temp)>0:
            subs.extend(temp)
    return subs

l1 = [10, 20, 30, 40]
l2 = ["X", "Y", "Z"]
print("Original list: ")
print(l1)
print("Sublist of the said list: ")
print(sub_lists(l1))
print("\nOriginal list: ")
print(l2)
print("Sublist of the said list: ")
print(sub_lists(l2))

#reference: w3resource