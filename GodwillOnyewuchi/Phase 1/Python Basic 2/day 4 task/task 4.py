
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
Character = input("Enter a character: ")

if Character in vowels:
    print(f'{Character} is a vowel')
else:
    print(f'{Character} is not a vowel')