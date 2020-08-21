'''
7. Write a Python program to accept a filename from the user and print the extension of that.
        Sample filename : abc.java
        Output : java
    Tools: input function, slicing
'''

#7
file_name = str(input('Enter the filename: '))
file_extn = file_name.split('.')
print('The file extension is: ' + repr(file_extn[-1]))