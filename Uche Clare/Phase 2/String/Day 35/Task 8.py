#Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings.
string='abcdpqr'
string1='xyzabcd'
common_char=list(set(string)^set(string1))
print('The uncommom characters are : ')
print(''.join(common))