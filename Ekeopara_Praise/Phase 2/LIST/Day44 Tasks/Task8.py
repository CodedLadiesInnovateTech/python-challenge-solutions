'''8. Write a Python program to replace the last element in a list with another list. 
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8] '''

lst1 = [1, 3, 5, 7, 9, 10]
lst2 = [2, 4, 6, 8]
lst3 = lst1[:-1] + lst2
print(lst3)