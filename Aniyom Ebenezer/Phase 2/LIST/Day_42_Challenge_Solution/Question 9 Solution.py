"""
Write a Python program to convert a list of multiple integers into a single integer.
"""
l = [11, 33, 50]
print("Original List: ", l)
x = int("".join(map(str, l)))
print("Single integer: ",x)