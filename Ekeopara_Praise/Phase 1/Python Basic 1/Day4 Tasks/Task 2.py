'''2. Write a Python program to count the number 4 in a given list.'''

lst_4 = [4, 5, 4, 6, 7, 2, 5, 6]
count = 0
lst = []
for i in lst_4:
    if i == 4:
        count = count + 1
print("The number of 4 in the list is: ",count)
    
