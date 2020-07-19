#Write a Python program to get the last part of a string before a specified character. 
str1 = "https://www.codedladiesinnovateyech.com/about-us"
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])