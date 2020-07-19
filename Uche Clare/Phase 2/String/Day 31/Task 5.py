#Write a Python program to create a Caesar encryption.
#Caesar encryption  It's simply a type of substitution cipher, i.e.
#each letter of a given text is replaced by a letter some fixed number of positions down the alphabet.
encrypted = "ABCDEFGHI"
shift = 5
minRange = ord('a')
print(minRange)
decrypted = ""
for char in encrypted:
    decrypted += chr(((ord(char) - minRange + shift) % 26) + minRange)
print(decrypted)
print(ord(char))

