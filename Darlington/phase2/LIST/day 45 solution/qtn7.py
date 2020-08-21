#program to find all the values in a list are greater than a specified number.
#num = [[4,5,6],[9,10,11],[13,8,2],[3,14,1]]

list1 = [220, 330, 500]
list2 = [12, 17, 21]
print(all(x >= 200 for x in list1))
print(all(x >= 25 for x in list2))