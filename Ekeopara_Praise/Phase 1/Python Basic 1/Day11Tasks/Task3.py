'''3. Write a Python program to get the identity of an object.'''
def get_identity(value):
    val_identity = type(value)
    return val_identity 
print(get_identity("abc"))
print(get_identity(234))
