#Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). 
word = 'Daniel'
word_copies = (word[-2:]*4)     #prints 4 copies of the last two characters
print(word_copies)