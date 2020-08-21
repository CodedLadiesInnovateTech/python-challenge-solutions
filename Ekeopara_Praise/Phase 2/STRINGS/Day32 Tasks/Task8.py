'''8. Write a Python program to count occurrences of a substring in a string.'''

def count_word_in_string(string1, substring2):
    return string1.count(substring2)
print(count_word_in_string('The quick brown fox jumps over the lazy dog that is chasing the fox.', "fox"))