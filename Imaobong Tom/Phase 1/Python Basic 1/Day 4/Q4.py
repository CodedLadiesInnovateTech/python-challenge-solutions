vowel = ["A", "E", "I", "O", "U"]
letter = input("Enter any letter:")
letter = letter.upper()
if letter in vowel:
    print (f"{letter} is a vowel")
else:
    print(f"{letter} is a consonant")
