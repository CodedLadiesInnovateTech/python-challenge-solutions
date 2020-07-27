'''5. Write a Python program to compute the product of a list of integers (without using for loop).'''
import math
from functools import reduce 
lst = [5, 4, 3, 2, 1]
ans = reduce(lambda x, y: x*y, lst, 1)
print(ans)