'''9. Write a Python program to get the difference between the two lists. '''

def difference_twoLists(lst1, lst2):
    lst1 = set(lst1)
    lst2 = set(lst2)
    return list(lst1 - lst2)
print(difference_twoLists([1, 2, 3, 4], [4, 5, 6, 7]))
print(difference_twoLists([1, 2, 3, 4], [0, 5, 6, 7]))
print(difference_twoLists([1, 2, 3, 4], [3, 5, 6, 7]))