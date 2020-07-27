#Write a Python program to remove a newline in Python. 
string = "The quick brown fox jumps over the lazy dog.\nThe quick brown fox jumps over the lazy dog."
print(string)
string= string.replace('\n', " ")           #Remove a newline
print(string)