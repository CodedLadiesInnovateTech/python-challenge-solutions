def multiply_string(string,no_times):
    result = ""
    if no_times<=0:
        print("please input a positive integer")
    else:
        for i in range(no_times):
            result=result+string
    return result
print(multiply_string("cup",-1))