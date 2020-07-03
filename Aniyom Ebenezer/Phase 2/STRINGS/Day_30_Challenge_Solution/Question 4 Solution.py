"""
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""
def sorted_words(str1):
    words = [word for word in str1.split(",")]
    print(",".join(sorted(list(words))))
sorted_words(input("Input a comma separated sequence of words: "))