
numbers = input("Enter a string of number: ")
num_strings = list(numbers)

if len(num_strings) > 2:
    print(num_strings[0:2])
else:
    print(num_strings)


