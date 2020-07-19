#Python program to remove a key from a dictionary.
myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict: 
    del myDict['a']
print(myDict)
if 'b' in myDict:
    del myDict['b']
print(myDict)    