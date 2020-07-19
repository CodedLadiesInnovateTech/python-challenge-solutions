"""
Write a python program to check whether two lists are circularly identical. 
"""
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]

print("Compare list1 and list2:")
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))