#Python program to get the smallest number from a list.
def least_num(list):
    min = list[ 0 ]
    for j in list:
        if j < min:
            min = j
    return min
print(least_num([2, 3, 1, 0, -3]))

def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([1, 2, -8, 0]))