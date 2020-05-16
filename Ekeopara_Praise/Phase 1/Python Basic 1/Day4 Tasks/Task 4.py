'''4. Write a Python program to test whether a passed letter is a vowel or not.'''

letr = str(input("Enter any letter: "))
vowel = ["A", 'a', "E", 'e', "I", 'i', "O", 'o', "U", 'u']

if letr in vowel:
    print("The letter entered is a vowel!")
else:
    print("The letter entered is not a vowel!")