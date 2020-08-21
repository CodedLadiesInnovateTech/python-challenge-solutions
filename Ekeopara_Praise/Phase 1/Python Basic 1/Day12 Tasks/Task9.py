'''9. Write a Python program to check if a number is positive, negative or zero.'''

def check_num(number):
    if number < 0:
        response = "Negative"
    elif number > 0:
        response = "Positive"
    else:
        response = "The number is Zero"
    return response

print(check_num(34))
print(check_num(-45))
print(check_num(0))




        