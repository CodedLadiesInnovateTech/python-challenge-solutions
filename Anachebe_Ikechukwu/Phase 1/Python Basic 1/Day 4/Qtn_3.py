#3. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

string= input("Enter a string of characters:")

n = int(input("Input the number of copies you want:"))

xy = string[0:2]
print(xy * n)