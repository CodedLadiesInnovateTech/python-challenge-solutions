'''1. Write a Python program to find the index of a given string at which a given substring starts. 
If the substring is not found in the given string return 'Not found'. '''

try:
    str1 = 'Obi is a boy'
    print(str1.index('BI'))
except:
    print("Not found")