#program that accepts a comma separated sequence of words as input and prints 
# the unique words in sorted form (alphanumerically).
items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))