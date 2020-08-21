"""Python program to accept a filename from the user and print the extension of that"""
file = input('enter file extension name: ')
new_file_name = file[file.index('.'):]
print(new_file_name)