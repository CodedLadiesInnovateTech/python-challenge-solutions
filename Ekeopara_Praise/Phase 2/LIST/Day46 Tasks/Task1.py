'''1. Write a Python program to check whether all dictionaries in a list are empty or not. 
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False '''

def check_dict(lst):
    
    if any(lst) == True:
        ans = 'False'
    else:
        ans = 'True'
    return ans

print(check_dict([{},{},{}]))
print(check_dict([{1, 2},{},{}]))