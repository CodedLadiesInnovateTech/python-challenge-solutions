'''3. Write a Python program to insert a given string at the beginning of all items in a list. 
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4'] '''

def add_string(lst1, str1):
    lst2 = []
    str(lst1)
    for i in lst1:
        var = str1 + str(i)
        lst2.append(var)
    return lst2
print(add_string([1, 2, 3, 4], 'emp'))