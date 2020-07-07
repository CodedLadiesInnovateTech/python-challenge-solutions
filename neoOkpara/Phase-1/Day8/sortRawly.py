from __future__ import print_function


number_list = []
for i in range(3):
    number = int(input("Input an Integer"))
    number_list.append(number)

number_list.sort()
print("See the resulting sorted list ", number_list)
