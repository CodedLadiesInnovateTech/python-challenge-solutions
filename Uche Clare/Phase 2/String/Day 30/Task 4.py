#Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
sequence = list(map(str, input('Enter words: ').split()))
print(sorted(sequence))