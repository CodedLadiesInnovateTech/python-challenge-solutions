'''7. Write a Python program to remove duplicates from a list. '''

testlist = ['a', 'a', 'b', 'b', 'c', 'c']
newlist = list(dict.fromkeys(testlist))
print(newlist)