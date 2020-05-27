'''5. Write a Python program to sum of all counts in a collection?'''
import collections
num = [3, 4, 5, 6, 3, 3, 4, 5, 7, 7, 8]
print(sum(collections.Counter(num).values()))


