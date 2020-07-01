'''8. Write a Python program to change the position of every n-th value with the (n+1)th in a list. 
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4] '''

from itertools import zip_longest, chain, tee
def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0,1,2,3,4,5]
print(replace2copy(n))

#Reference: w3resource