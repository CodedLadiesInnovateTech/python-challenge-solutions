"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
"""
x = float(input("x = "))
y = float(input("y = "))
f = int(y/2)
def GCD(x,y):
    GCD = 1
    if x%y == 0:
        return y
    for a in range(f,0,-1):
        if x%a == 0 and y%a == 0:
            GCD = a
            break
    return GCD
print(GCD(x,y))