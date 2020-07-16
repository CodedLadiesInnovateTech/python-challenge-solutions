"""
Write a Python script to sort (ascending and descending) a dictionary by value.
"""
import operator
dict1 = {'b': 5, 'i': 3, 'm': 1, 'a': 8}
print("Original Dictionary List: \n{}".format(dict1))
dict1_sorted = dict(sorted(dict1.items(), key=operator.itemgetter(1)))
print("The Sorted Values in ascending Order is: \n{}".format(dict1_sorted))
dict1_sorted2 = dict(sorted(dict1.items(), key=operator.itemgetter(1), reverse=True))
print("The Sorted Values in ascending Order is: \n{}".format(dict1_sorted2))