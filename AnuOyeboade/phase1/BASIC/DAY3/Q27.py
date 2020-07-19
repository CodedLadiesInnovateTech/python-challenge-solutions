"""
Write a Python program to concatenate all elements in a list into a string and return it.
"""
s = list(input("Enter a list"))
t = ''.join([str(elem) for elem in s])
print(t)