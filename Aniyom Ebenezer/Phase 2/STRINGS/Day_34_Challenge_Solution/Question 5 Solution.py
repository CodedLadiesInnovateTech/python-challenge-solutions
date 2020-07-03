"""
Write a Python program to find the first repeated word in a given string.
"""
def first_repeated_word(str1):
    temp = set()
    for word in str1.split():
        if word in temp:
            return word
        else:
            temp.add(word)
    return "None"
print(first_repeated_word("ab ca bc ab"))