'''1. Write a Python function that takes a sequence of numbers and determines whether 
all the numbers are different from each other.'''

def unique(string):
    if len(string) == len(set(string)):
        ans = 'True'
    else:
        ans = 'False'
    return ans

print(unique((1, 2, 3, 4)))
print(unique((1, 3, 3, 4)))
