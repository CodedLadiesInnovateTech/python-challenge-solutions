'''7. Write a Python program to extract single key-value pair of a dictionary in variables.'''
d = {'foo': 'bar'}
(k, v), = d.items()
print(k)