#Write a Python program to create two strings from a given string.
#Create the first string using those character which occurs only once and create the second string which consists
# of multi-time occurring characters in the said string.
str1=input('enter string:')
str2=''
str3=''
for i in str1:
    if str1.count(i)>1:
        str2+=i
    else:
        str3+=i
print(str2)                     #mult-time occurring character 
print(str3)                     #The rest of the character