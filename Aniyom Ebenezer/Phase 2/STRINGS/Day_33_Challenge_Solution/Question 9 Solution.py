"""
Write a Python program to count and display the vowels of a given text.
"""
text = "pyladies"
vowels = "aeiouAEIOU"
print(len([letter for letter in text if letter in vowels]))
print([letter for letter in text if letter in vowels])