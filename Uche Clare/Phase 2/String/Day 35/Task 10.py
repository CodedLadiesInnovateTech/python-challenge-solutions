#Write a Python program to find the longest common sub-string from two given strings. 
str1='i love Jesus and he loves me too '
str3='Jesus is my Lord and Saviour'
str2= sorted(str3.split(' '),key=len)
for i in sorted(str1.split(' '),key=len):
    for j in str2:
        if i == j:
            result = max(i, j, key=len)

print(result)