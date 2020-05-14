#program to show LIST and TUPLE
nums = input("ENTER SOME COMMA SEPARATED VALUES/NUMBERS: ")
list = nums.split(",")
tuple = tuple(list)
print(list)
print(tuple)