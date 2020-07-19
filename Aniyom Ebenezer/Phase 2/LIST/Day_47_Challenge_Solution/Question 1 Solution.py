"""
Write a Python program to extract a given number of randomly selected elements from a given list.
"""
import random
n_list = [1, 2, 3, 4, 7, 8, 4, 9]
n = 3
print("Original List: \n{}".format(n_list))
print()
print("Randomly selected elements from the list: ")
print(random.sample(n_list, n))