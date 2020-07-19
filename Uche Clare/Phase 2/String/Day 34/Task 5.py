#Write a Python program to find the first repeated word in a given string.
def repeated_word(word):
    word1 = word.split()
    for i in word1:
        if word1.count(i) > 1:
            return i

print(repeated_word('ab ba cca dc cca ab'))