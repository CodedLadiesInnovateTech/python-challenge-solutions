''' 8. Write a Python program to check a list is empty or not.  '''

def check_list(lst):
    if len(lst) == 0:
        ans = "List is empty"
    else:
        ans = "List not empty"
    return ans
print(check_list([1, 2, 3]))
print(check_list([]))
print(check_list([1]))
print(check_list([]))
