'''8. Write a Python function that takes a list of words and returns the length of the longest one. '''

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    
    return max(word_len)

print(find_longest_word(["PHP", "Exercises", "International"]))
