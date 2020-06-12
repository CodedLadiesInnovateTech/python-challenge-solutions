
#4. Write a Python program to test whether a passed letter is a vowel or not.

string = input("Enter a vowel letter:")



vowel = ['a','e','i','o','u']


if string.lower() in vowel:
    print(string + " is a vowel")


else:
    print(string + " is a consonant")