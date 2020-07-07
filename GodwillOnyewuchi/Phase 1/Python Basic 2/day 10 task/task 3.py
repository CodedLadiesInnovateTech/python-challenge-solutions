# Python program to test whether all numbers of a list is greater than a certain number

List = [1, 3, 45, 5, 4, 7, 0, 8, 3, 6, 6, 46, 3]
checkList = []

for i in List:
    if i > 12:
        checkList.append(i)
if len(checkList) == len(List):
    print(f'All of the numbers in the list are  above 12')
else:
    print(f'All of the numbers in the list are not above 12')
