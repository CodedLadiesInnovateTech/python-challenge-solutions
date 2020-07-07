"""
 Write a Python program to get unique values from a list. 
"""
list1 = [10, 20, 30, 40, 20, 60, 40, 90]
print("Original list: ",list1)
set1 = set(list1)
list2 = list(set1)
print("List of unique numbers: ", list2)