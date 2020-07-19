'''1. Write a Python program to split a list every Nth element. 
Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']] ''' 

def split_list(lst, splitnum):
    splitedlist = [lst[i * splitnum: (i + 1) * splitnum] for i in range((len(lst) + splitnum-1)//splitnum)]
    return splitedlist
print(split_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 8], 3))