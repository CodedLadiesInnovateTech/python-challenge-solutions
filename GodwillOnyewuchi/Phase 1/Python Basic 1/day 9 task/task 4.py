#Python program to hash a word

check_codes = [0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0, 3, 5, 0, 1, 2, 7, 3, 4, 0, 6, 4, 3, 0, 2]

word = input("Input the word be hashed: ")

word = word.upper()

codes = word[0]

for a in word[1:len(word)]:
    i = 65 - ord(a)
    codes = codes + str(check_codes[i])

print("The coded word is: " + codes)
