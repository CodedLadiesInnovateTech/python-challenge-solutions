# Store Vowels in a List and Check if the passed string contains any of the vowel stored
vowels = ["a", "e", "i", "o", "u"]


def is_it_vowel(string):
    message = "not vowel"
    for x in vowels:
        if string == x:
            message = "vowel"
    return message


print(is_it_vowel("a"))
print(is_it_vowel("b"))
