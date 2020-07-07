# Python program to count the number occurrence of a specific character in a string

String = input("Enter a string: ")

Alphabet = input("Enter the alphabet to find: ")

count = 0
for i in String:
    if i == Alphabet:
        count += 1
print(f'{Alphabet} coccured {count} times in {String}')