'''9. Write a Python program to convert a list of multiple integers into a single integer. 
Sample list: [11, 33, 50]
Expected Output: 113350 '''

def convert_list(lst1):
    lst2 = [str(i) for i in lst1]
    lst3 = int(''.join(lst2))
    return lst3
print(convert_list([11, 33, 50]))