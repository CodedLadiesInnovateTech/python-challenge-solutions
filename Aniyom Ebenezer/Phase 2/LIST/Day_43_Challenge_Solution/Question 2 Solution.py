"""
Write a Python program to find missing and additional values in two lists.
"""
list1 = ["a", "b", "c", "d", "e"]
list2 = ["d", "e", "f", "g", "h"]
print("The missing values in list2 are: ", (set(list1).difference(set(list2))))
print("The additional values in list1 are: ", (set(list2).difference(set(list1))))