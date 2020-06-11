#8. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
 #   Tools: math, input function

a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
c = int(input("Enter a third number:"))

x = a + b + c

if (a == b == c):
    print( x * 3)

else:
    print(x)