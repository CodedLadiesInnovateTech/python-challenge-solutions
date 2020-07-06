'''8. Write a Python program to extend a list without append. 
Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30] '''

lst1 = [10, 20, 30]
lst2 = [40, 50, 60]
lst3 = lst2 + lst1
print(lst3)