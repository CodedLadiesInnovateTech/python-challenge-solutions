#Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
num = list(map(int, input('Numbers: ').split()))  
print(num)
x = num[0]
y = num[0]
for i in num:
    if i > x:
        x = i
    elif i < y:
        y= i
print('The maximum and minimum number is: ')
print(x, 'and', y)