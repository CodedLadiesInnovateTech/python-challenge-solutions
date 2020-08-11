#program to use of frozensets.
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
#use isdisjoint(). Return True if the set has no elements in common with other. 
print(x.isdisjoint(y))
#use difference(). Return a new set with elements in the set that are not in the others.
print(x.difference(y))
#new set with elements from both x and y
print(x | y)