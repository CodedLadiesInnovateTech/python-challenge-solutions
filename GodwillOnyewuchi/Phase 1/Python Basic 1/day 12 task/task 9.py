# Python program to check if a number is positive, negative or zero

num = int(input("Enter a number: "))

if num == 0:
    print("Number is Zero")
elif num + abs(num) == 0:
    print("Number is Negative ")
else:
    print("Number is positive")
