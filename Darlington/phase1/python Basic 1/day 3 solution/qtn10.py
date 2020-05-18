#program to get string which is n
word = input('Enter numbers \n')
texts = list(word)
print(f'{texts}')
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
integer = ""
for i in texts:
    if i in numbers:
        integer += i
print(integer)
