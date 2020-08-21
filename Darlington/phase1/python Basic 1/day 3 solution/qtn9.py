#program to get a new string from a given string
text = input('Enter a text \n')
li = 'Is'
if li in text:
    print(text)
else:
    print(text[:-2])
