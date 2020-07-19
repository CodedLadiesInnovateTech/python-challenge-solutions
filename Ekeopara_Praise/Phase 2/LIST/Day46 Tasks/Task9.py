'''9. Write a Python program to remove the K'th element from a given list, print the new list. 
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splited the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1]) '''

lst1 = [1, 1, 2, 3, 4, 4, 5, 1]

print("Original List:\n", lst1)
print('')
print('K\'th element to be removed = 5')
print('')

lst1.pop(5)
print("List after removal:\n", lst1)