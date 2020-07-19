'''
 Write a Python program to get unique values from a list. 
'''
import collections
list1 = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 40, 50, 50, 30]
print("Original List: ",list1)
ctr = collections.Counter(list1)
print("Frequency of the elements in the list: ", ctr)