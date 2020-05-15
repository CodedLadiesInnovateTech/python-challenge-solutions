"""Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers"""
numbers = input('enter a list of numbers ').replace(',','')
li_number = list(numbers)
tu_number = tuple(numbers)
print(li_number)
print(tu_number)