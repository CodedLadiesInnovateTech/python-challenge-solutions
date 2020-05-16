def multiple_string(string, number_of_times):
    result = ""
    if number_of_times <= 0:
        print("input a positive integer")
    for i in range(number_of_times):
        result = result + string
    return result
print(multiple_string("cup",0))
