'''
6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
        Sample data : 3, 5, 7, 23
        Output :
        List : ['3', ' 5', ' 7', ' 23']
        Tuple : ('3', ' 5', ' 7', ' 23')
    Tools: input function, list, tuple
'''

#6
nums = input('Enter your comma-separated numbers: ')
lst = list(nums.split(sep= ','))
tpl = tuple(lst)
print('List: ', lst)
print('Tuple: ', tpl)