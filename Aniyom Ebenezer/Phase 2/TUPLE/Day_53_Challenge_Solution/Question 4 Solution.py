'''
Write a Python program to find the index of an item of a tuple.
'''
tuplex = tuple("index tuple")
print(tuplex)
index = tuplex.index("p")
print(index)
index = tuplex.index("p", 5)
print(index)
index = tuplex.index("e", 3, 6)
print(index)
index = tuplex.index("y")