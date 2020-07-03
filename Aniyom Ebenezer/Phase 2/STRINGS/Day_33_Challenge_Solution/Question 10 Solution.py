"""
 Write a Python program to split a string on the last occurrence of the delimiter
"""
str1 = "p,y,l,a,d,i,e,s"
print(str1.rsplit(',', 1))
print(str1.rsplit(',', 2))
print(str1.rsplit(',', 5))