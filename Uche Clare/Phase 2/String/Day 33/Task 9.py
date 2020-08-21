#Write a Python program to count and display the vowels of a given text.
samp_string = "extensions"
count = 0
vowels ="AEIOUaeiou"
for i in samp_string:
    if i in vowels:
        count += 1
        print('The vowels are:', i )
print(f'They are {count} in number')

        