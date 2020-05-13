constant_number = 17


def calculate_diff(number):
    value = 0
    if number > constant_number:
        value = abs(constant_number - number) * 2
    else:
        value = constant_number - number
    return value


inputted_no = int(input("Enter your number: "))

print (calculate_diff(inputted_no))
