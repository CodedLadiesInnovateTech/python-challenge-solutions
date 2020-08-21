'''8. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splited the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1]) '''

def split_two_parts(n_list, L):
    return n_list[:L], n_list[L:]
n_list = [1,1,2,3,4,4,5, 1]
print("Original list:") 
print(n_list)
first_list_length = 3
print("\nLength of the first part of the list:",first_list_length)
print("\nSplited the said list into two parts:")
print(split_two_parts(n_list, first_list_length))