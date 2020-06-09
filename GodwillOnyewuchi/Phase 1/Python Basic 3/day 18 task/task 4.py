# Write a Python program to add two positive integers without using the '+' operator

a = 34
b = 2

while b != 0:
    data = a & b
    a = a ^ b
    b = data << 1

print(a)
