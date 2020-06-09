'''3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.'''

def remove_nums(int_list):
    position = 3 - 1
    idx = 0
    len_list = (len(int_list))
    while len_list>0:
        idx = (position+idx)%len_list
        print(int_list.pop(idx))
        len_list -=1
print(remove_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
