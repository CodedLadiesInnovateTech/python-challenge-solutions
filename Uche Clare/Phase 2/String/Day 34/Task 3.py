#Write a Python program to find the first repeated character in a given string.
def repeated_char(string):
    for i in string:
        if string.count(i) > 1:
            return i
print(repeated_char("wmmcjjf"))
print(repeated_char("ghdssd"))