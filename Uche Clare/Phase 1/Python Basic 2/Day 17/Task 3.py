#Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
num = [1, 3, 4, 5, 6, 9, 10, 1, 1]
while len(num)!= 0:
    print(num[2])
    del(num[2])
print(num)
