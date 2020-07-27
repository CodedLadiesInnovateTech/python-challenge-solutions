#Write a Python function to create the HTML string with tags around the word(s). 
word = 'Welcome to my webpage'
tag= input('Enter tag: ')
print('<%s> %s </%s>' % (tag, word,tag))