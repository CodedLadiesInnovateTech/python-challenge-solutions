'''
Write a Python program to print without newline or space.
'''

data1 = input("Just enter some data: ")
data2 = input("You can tell more stories: ")

print('The writeup above is printed without spacing. \n')
print(data1, data2, sep="", end="\n\n")