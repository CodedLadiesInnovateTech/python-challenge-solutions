''' Write a Python program to accept a filename from the user and print the extension of that. '''
ext = input("Enter a file name: ")
files = ext.split('.')
print(files[1])
