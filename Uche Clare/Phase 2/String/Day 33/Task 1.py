#Write a Python program to strip a set of characters from a string. 
strip_string = "**@clare**#@#@"
print()
print(strip_string.rstrip("*@#"))               #this strips the characters given from the right side
print()
print(strip_string.lstrip("*"))                 #this strips characters given from the left side
print()
print(strip_string.strip("#@*"))                #this strips the entire characters given