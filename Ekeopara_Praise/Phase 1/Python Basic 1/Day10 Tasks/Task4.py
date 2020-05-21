'''4. Write a Python program to count the number occurrence
of a specific character in a string.'''

def count_character(string, char):
    return string.count(char)
    
print(count_character("Stackoverflow", 'o'))
print(count_character("Hash", 's'))


