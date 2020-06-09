"""
Write a Python program to add two positive integers without using the '+' operator
Note: Use bitwise operations to add two numbers
"""
a = int(input("Input a Number: "))
b = int(input("Input another number: "))
while b != 0:
    data = a & b
    a = a ^ b
    b = data << 1
    print("The sum of the two positive numbers is: ",a)