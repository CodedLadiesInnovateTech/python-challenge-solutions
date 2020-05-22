'''10. Write a Python program to create a copy of its own source code.'''
with open(__file__) as f:
    print(f.read())

#Example
print("output:\nThis is just an example")
