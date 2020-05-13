"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""
n = int(input("Enter a positive integer:"))
if n<0:
    print("Enter a positive integer")
else:
    n1 = str(n)
    n2 = n1+n1
    n3 = n1+n1+n1
    value = n + int(n2)+int(n3)
    print("Result = " ,value)
