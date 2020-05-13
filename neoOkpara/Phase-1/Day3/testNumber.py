def check_number(param):
    result = "False"
    if(abs(1000 - param) <= 100) or (abs(2000 - param) <= 100):
        result = "True"
    return result


inputted_no = int(input("Enter number here: "))

print (check_number(inputted_no))
