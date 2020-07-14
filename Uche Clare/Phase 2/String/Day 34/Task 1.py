#Write a Python program to find the first non-repeating character in given string.
def non_repeating_char(string):
    for i in string:
        if string.count(i)==1:
            return i
print('The non repeating character are:')
print(non_repeating_char("cocopops"))
print('and')
print(non_repeating_char("iterating"))