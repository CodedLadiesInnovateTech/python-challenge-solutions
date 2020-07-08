#Write a Python program to split a string on the last occurrence of the delimiter.
str1 = "P,Y,T,H,O,N"
print(str1.rsplit(',', 1))
print(str1.split(',', 2))
print(str1.split(',', 3))