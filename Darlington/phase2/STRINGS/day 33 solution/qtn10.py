# program to split a string on the last occurrence of the delimiter.
str1 = "w,3,r,e,s,o,u,r,c,e"
print(str1.rsplit(',', 1))
print(str1.rsplit(',', 2))
print(str1.rsplit(',', 5))