# program to find the list in a list of lists whose sum of elements is the highest.
num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
print(max(num, key=sum))