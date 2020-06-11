#10. Write a Python program to get a string which is n (non-negative integer) copies of a given string.
#   Tools: input function, slicing

str = input("Enter is string:")
n = int(input("Enter a positive integer:"))

xy = slice(n)

print(str[xy])