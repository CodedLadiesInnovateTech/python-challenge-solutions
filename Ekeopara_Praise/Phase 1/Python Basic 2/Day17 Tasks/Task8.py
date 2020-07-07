'''8. Write a Python program to find the median among three given numbers.'''

def median(lst):
    new_list = sorted(lst)
    med = new_list[1]
    return med
print(median([3, 2, 1]))
print(median([3, 1, 2]))
print(median([1, 2, 3]))



