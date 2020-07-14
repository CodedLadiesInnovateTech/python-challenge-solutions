"""
Write a Python program to check whether all dictionaries in a list are empty or not.
"""
my_list = [{}, {}, {}]
my_list1 = [{1, 2}, {}, {}]
print(all(not d for d in my_list))
print(all(not d for d in my_list1))