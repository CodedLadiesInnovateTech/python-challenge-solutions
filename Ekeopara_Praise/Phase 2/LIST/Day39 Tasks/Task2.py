'''2. Write a Python program to multiplies all the items in a list. '''

from operator import mul
from functools import reduce
def multi_items_in_list(lst):
    ans = reduce(mul, lst, 1)
    return ans
print(multi_items_in_list([1, 2, 3, 4, 5]))