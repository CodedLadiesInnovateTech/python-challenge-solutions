#program to print letters from the English alphabet from a-z and A-Z.
import string
print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
   print(letter, end =" ")
print("\nAlphabet from A-Z:")
for letter in string.ascii_uppercase:
   print(letter, end =" ")