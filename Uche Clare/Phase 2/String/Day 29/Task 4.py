#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
samp_string = input('Enter String:')
samp = samp_string[0]                               #this prints the first character

samp_string = samp_string.replace(samp, '$')        #it replaces the first char with $
result = samp + samp_string[1:]                     #the result print any letter with the char expect the first letter

print(result)