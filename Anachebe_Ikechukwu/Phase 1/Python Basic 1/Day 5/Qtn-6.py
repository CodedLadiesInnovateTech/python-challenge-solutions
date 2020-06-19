#6. Write a Python program to add two objects if both objects are an integer type.

def add_obj(a, b):
    if (isinstance(a, int) and isinstance(b, int)):
        return a + b

    else:
        return TypeError("Must be integer numbers")

print(add_obj(30, 30))
