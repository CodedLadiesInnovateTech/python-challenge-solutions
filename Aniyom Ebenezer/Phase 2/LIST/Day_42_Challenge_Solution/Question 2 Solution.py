"""
Write a Python program to check whether a list contains a sublist.
"""
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [1, 3, 5, 7, 9]
set1 = set(list1)
set2 = set(list2)
print(set2 in set1)