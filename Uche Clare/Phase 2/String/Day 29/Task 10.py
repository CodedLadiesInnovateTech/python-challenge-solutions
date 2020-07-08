#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
word = input('Enter the word: ')
letter_exchanger = word[-1] + word[1:-1] + word[0]                  #first and last character exchanger
print(letter_exchanger)