def type(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a+b
    return 'Not integer type'

print(type(2,3))
print(type('a','boy'))