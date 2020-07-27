def is_vowel(n):
    vowel = ['a','e','i','o','u']
    if n in vowel:
        return 'This letter is a vowel'
    else:
        return 'This letter is not a vowel'


print(is_vowel('i'))
print(is_vowel('b'))
