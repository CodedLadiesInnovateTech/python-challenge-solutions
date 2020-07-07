#program to test whether all numbers of a list is greater than a certain number.
list=[43, 12, 31, 17, 27]
a= int(input('Number: '))
for i in list:
 if i <= a:
    print('True')
    break
else:
    print('False')