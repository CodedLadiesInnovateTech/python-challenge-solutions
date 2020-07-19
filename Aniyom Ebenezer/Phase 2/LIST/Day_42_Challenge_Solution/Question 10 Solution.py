"""
Write a Python program to split a list based on first character of word.
"""
from itertools import groupby
from operator import itemgetter
word_list = ["be", "have", 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'look', 'want', 'give', 'ask']
for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)