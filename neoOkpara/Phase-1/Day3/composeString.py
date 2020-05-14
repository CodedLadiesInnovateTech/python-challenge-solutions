def compose_string(inputted_str, number):
    result = ""
    while number > 0:
        result += inputted_str
        number -= 1
    return result


sample_string = raw_input("Input the string: ")
sample_no = int(input("How many times do you want it repeated: "))

value = compose_string(sample_string, sample_no)
print (value)
