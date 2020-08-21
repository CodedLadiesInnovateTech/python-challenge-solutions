def check_number():
    num = int(input("Enter a number:"))
    test_data = [1, 5, 8, 3]
    if num in test_data:
        return print(True)
    else:
        return print(False)
check_number()