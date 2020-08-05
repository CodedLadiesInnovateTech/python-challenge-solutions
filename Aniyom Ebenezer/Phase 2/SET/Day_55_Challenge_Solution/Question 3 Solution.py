'''
Write a Python program to add member(s) in a set.
'''
set1 = set([2, 4, 8, 10])
num = [1]
print("Origin set without the new member is: {}".format(set1))
print()
set1.update(num)
print("New set with the new member is: {}".format(set1))