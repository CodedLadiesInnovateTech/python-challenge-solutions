"""
Write a Python program to remove the nth index character from a nonempty string.
"""
def remove_char(str, n):
    first_char = str[:n]
    last_char = str[n+1:]
    return first_char + last_char
print(remove_char("Python", 0))
print(remove_char("Ebenezera", 8))