'''5. Write a Python program to create a list reflecting the run-length encoding from a given list of
 integers or a given list of characters. 
Original list:
[1, 1, 2, 3, 4, 4.3, 5, 1]
List reflecting the run-length encoding from the said list:
[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
Original String:
automatically
List reflecting the run-length encoding from the said string:
[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], 
[1, 'y']] '''

from itertools import groupby
def encode_list(s_list):
    return [[len(list(group)), key] for key, group in groupby(s_list)]
n_list = [1,1,2,3,4,4.3,5, 1]
print("Original list:") 
print(n_list)
print("\nList reflecting the run-length encoding from the said list:")
print(encode_list(n_list))
n_list = 'automatically'
print("\nOriginal String:") 
print(n_list)
print("\nList reflecting the run-length encoding from the said string:")
print(encode_list(n_list))

#Reference: w3resource