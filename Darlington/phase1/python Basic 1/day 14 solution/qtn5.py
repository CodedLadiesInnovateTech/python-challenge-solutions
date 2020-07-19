#program to sum of all counts in a collections.
import collections
num = [2,2,4,6,6,8,6,10,4,40,5,8,4,6,7,8]
print(sum(collections.Counter(num).values()))