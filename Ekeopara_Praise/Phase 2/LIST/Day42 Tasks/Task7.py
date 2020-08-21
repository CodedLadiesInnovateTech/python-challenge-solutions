'''7. Write a Python program to find common items from two lists. '''
lst1 = [1, 'b', 'a', 2, 3, 4 , 5]
lst2 = [0, 9, 'a', 8, 7, 'b', 6]
lst3 = set(lst1) & set(lst2)
print("The common items in the two lists are:\n", list(lst3))