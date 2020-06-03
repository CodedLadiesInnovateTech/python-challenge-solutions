# Write a Python program to empty a variable without destroying it.

n = 20
d = {"x" : 200}

n = type(n)()
d = type(d)()

print(n, d)
