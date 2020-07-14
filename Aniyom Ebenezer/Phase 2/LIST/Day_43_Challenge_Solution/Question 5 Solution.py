"""
Write a Python program to convert a pair of values into a sorted unique array.
"""
l = [
    (1, 2),
    (3, 4),
    (5, 6),
    (7, 8),
    (9, 10)
]
print("Original list: ",l)
print("Sorted Unique data set: ",sorted(set().union(*l)))