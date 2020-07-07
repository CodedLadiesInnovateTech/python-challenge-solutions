#Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. 
string = input('Enter String: ')
case = 0
for i in string[0:4]:
    if i.upper()==i:
        case+=1
if case >= 2:
            print(string.upper())
else:
    print(string)