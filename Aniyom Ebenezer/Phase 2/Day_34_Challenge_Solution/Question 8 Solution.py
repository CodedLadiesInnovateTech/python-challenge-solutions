"""
Write a Python program to move spaces to the front of a given string.
"""
str1 = "codedladies innovate . com"
noSpaces_char = [ch for ch in str1 if ch != ' ']
spaces_char = len(str1) - len(noSpaces_char)
result = ' '*spaces_char
result = '"'+result + ''.join(noSpaces_char)+'"'
print(result)