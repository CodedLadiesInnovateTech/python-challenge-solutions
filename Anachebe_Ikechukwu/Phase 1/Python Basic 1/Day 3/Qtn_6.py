#6. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
#    Tools: abs function, input function, math

abs = int(input("Enter an integer greater than 17:"))

x = abs - 17
if abs > 17:
    print (x * 2)
