#Write a Python program to remove duplicate characters of a given string.
string = "Python programming"
le = ""
for i in string:
    if i not in le:
        le = le + i
print(le)