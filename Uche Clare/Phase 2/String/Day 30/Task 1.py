#Write a Python program to remove the characters which have odd index values of a given string
word = 'Codedladies'
print(word[0::2])                                                                   #odd index character remover


#OR 

word = 'Codedladies'
join = " "
for i in range(len(word)):
    if i%2==0:
     join = join + word[i]
print(join)

