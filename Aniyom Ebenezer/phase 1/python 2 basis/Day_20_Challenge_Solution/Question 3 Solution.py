"""
Write a Python program to compute the digit number of sum of two given integers
"""
a, b = map(int, input("Input two integers(a, b): ").split(" "))
print("Number of digit of a and b: ", len(str(a+b)))