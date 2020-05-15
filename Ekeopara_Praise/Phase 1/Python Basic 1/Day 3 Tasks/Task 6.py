'''6. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
    Tools: abs function, input function, math'''


#num = int(input("Enter a number greater than 17: "))

def num_difference(num):
    if num <= 17:
        return 17 - num
    else:
        return (abs(num - 17))*2

print(num_difference(20))
