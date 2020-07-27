'''10. Write a Python program to sum all the items in a dictionary.'''

def returnSum(myDict): 
    sum = 0
    for i in myDict: 
        sum = sum + myDict[i] 
    return sum

print(returnSum({'a': 200, 'b': 300}))