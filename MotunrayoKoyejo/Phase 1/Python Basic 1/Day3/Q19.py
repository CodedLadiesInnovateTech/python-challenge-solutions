def add(phrase):
    if len(phrase) >=2 and phrase[:2] == 'Is':
        return phrase
    else:
         return 'Is' + phrase

print(add('Motune'))
print(add('Ismotune'))