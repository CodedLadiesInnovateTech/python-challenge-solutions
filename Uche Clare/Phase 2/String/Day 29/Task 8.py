#Write a Python function that takes a list of words and returns the length of the longest one. 
words = ['opportunity', 'carriage', 'confidence', 'compatibilities', 'pronunciation']
lngst_word = max(words, key=len)
print(f'The longest word is {lngst_word} and its length is', len(lngst_word))