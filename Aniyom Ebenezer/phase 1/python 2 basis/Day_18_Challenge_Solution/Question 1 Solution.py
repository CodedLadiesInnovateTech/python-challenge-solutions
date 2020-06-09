"""
Write a Python program to check the sum of thre elements(each from an array) from three arrays is equal to a 
target value. print all those three element combinations.

Sample data:
/*
X = [10,20,20,20]
Y = [10,20,30,40]
Z = [10,30,40,20]
target = 70
"""

import itertools
from itertools import partial
X = [10,20,20,20]
Y = [10,20,30,40]
Z = [10,30,40,20]
T = 70

def check_sum_array(N, *nums):
    if sum(x for x in nums) == N:
        return(True, nums)
    else:
        return(False, nums)
pro = itertools.product(X,Y,Z)
func = partial(check_sum_array, T)
sums = list(itertools.starmap(func, pro))


result = set()
for s in sums:
    if s[0] == True and  s[1] not in result:
        result.add(s[1])
        print(result)