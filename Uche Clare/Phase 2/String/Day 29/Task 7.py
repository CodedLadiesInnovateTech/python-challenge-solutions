#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. 
samp_string1 = 'The lyrics is not that poor '
samp_string2 = 'The lyrics is poor'
if 'not' in samp_string1 and 'poor' in samp_string1:
    print('The lyrics is good!')
else:
    print('The lyrics is poor')



c= samp_string1.replace('not that poor' , "good")
print(c)