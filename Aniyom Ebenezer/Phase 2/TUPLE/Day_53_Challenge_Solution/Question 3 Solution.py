'''
Write a Python program to slice a tuple.
'''
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
slice = tuplex[3:5]
print(slice)
_slice = tuplex[:6]
print(_slice)
_slice = tuplex[5:]
print(_slice)
_slice = tuplex[:]
print(_slice)
_slice = tuplex[-8:-4]
print(_slice)
tuplex = tuple("HELLO WORLD")
print(tuplex)
_slice = tuplex[2:9:2]
print(_slice)
_slice = tuplex[::4]
print(_slice)
_slice = tuplex[9:2:-4]
print(_slice)