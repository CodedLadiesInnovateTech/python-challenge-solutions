# Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies

Text = 'This is the name of the boy'

words = Text.split()

word_freq = [words.count(n) for n in words]

print(f'Text = {Text}')
print(f'Words = {words}')
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(words, word_freq)))))