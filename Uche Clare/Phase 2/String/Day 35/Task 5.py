#Write a Python program to find all the common characters in lexicographical order from two given lower case strings.
#If there are no common letters print "No common characters".

str1 = input("Enter a string:")
str2 = input("Enter a string:")
m = ""
for i in str1:
    for j in str2:
        if i == j:
            m+= i

print(set(m))