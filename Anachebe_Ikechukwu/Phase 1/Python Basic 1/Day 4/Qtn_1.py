
#1. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

x = int(input("Enter a number:"))

if x % 2 == 0:
    print("This is an even number")

else:
    print("This is an odd number")