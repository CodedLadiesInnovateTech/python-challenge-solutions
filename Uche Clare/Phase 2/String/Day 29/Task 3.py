#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
string_1 = input('Input a String: ')
if len(string_1) == len(string_1):          
    print(string_1[0:2]+string_1[-2:])           #return first 2 and last 2 characters from the string 

elif len(string_1) == 1:
    print(' ')                          #return an Empty String
                        
elif len(string_1) < 2:                          #return twice the string if length is less than 2
    print(string_1*2)



