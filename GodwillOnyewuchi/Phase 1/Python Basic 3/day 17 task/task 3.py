# Write a Python program to remove and print every third number from a list of numbers until the list becomes empty

List = [1, 2, 3, 4, 5, 6, 6, 7, 8]

while len(List) > 3:
    List.pop(2)
    print(List[2])

print(List)
