"""
Write a Python program that takes a list of words and retuerns the length of the longest one.
"""
def longest_words(word_list):
    word_len = []
    for n in word_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]
print(longest_words(["PHP", "Python", "Backend"]))