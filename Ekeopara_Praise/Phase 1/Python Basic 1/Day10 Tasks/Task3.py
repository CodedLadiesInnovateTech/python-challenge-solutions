'''3. Write a Python program to test whether all
numbers of a list is greater than a certain number.'''

def check_list(lst, certain_num):
    for num in lst:
        if num > certain_num:
            reply = "True"
        else:
            reply = "False"
    return reply
print(check_list([1, 3, 5, 2, 2], 10))
print(check_list([7, 7, 8, 9, 10], 6))