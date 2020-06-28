"""
Write a Python program to print four values decimal, octal, hexadecimal (capitlized),
binary in a single line of a given integer.
Sample Output:
Input an Integer: 25
Decimal Octal Hexadecimal (capitalized), Binary
25 31 19 19 11001
"""
i = int(input("Input an Integer: "))
o = str(oct(i))[2:]
h = str(hex(i))[2:]
h = h.upper()
b = str(bin(i))[2:]
d = str(i)
print("Decimal Octal Hexadecimal (capitalized), Binary")
print(d,'  ',o,' ',h,'          ',b)