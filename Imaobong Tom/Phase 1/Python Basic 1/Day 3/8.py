def calculate ():
    a = float(input("Enter 1st number:"))
    b = float(input("Enter 2nd number:"))
    c = float(input("Enter 3rd number:"))
    sum = a + b + c
    if a == b == c:
        return 3*sum
    else:
        return sum
print(calculate())



