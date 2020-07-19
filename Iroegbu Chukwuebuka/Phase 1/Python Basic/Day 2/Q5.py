"""Python program which accepts the user's first and last name and print them in reverse order with a space between them"""
name = input('enter your names: ')
new_name = name[name.index(' '):] + ' ' +name[0:name.index(' ')]
print(new_name)