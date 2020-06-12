'''5. From Wikipedia:
An isogram (also known as a "nonpattern word") is a logological term for a word or phrase without a repeating letter. It is also used by some people to mean a word or phrase in which each letter appears the same number of times, not necessarily just once. Conveniently, the word itself is an isogram in both senses of the word, making it autological.
Write a Python program to check whether a given string is an "isogram" or not.
Sample Output:
False
True
True
False'''
def check_isogram(str1):
    return len(str1) == len(set(str1.lower()))

print(check_isogram("w3resource"))
print(check_isogram("w3r"))
print(check_isogram("Python"))
print(check_isogram("Java"))

#Reference: w3resource