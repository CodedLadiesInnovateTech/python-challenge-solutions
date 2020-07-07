vow = ["a", "e", "i", "o", "u"]

word = input("Enter a letter: ")

if word.lower() in vow:
    print("You entered the Vowel {}.".format(word))
else:        
    print("That's a Consonant!")