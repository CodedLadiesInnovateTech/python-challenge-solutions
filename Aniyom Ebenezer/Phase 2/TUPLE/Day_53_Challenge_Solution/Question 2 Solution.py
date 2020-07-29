'''
Write a Python program to remove an item from a tuple.
'''
tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
listx = list(tuplex) 
listx.remove("c") 
tuplex = tuple(listx)
print(tuplex)