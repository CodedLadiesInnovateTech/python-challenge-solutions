fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = int(input("Enter your age: "))

print('''First name: {0}
Last name: {1}
Age: {2}'''.format(fname.capitalize(), lname.upper(), age))
