#Python program to extend a list without append.
x = [10, 20, 30]
y = [40, 50, 60]
z = [70, 80, 90]
x[:0] = y
print(x)
x[:0] = z
print(x)