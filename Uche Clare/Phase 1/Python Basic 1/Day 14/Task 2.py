'''Write a Python program to empty a variable without destroying it.
Sample data: n=20
d = {"x":200}
Expected Output : 0
{}'''

n = 20
d = {"x":200}
print(type(n)())
print(type(d)())