def form_string(input_string):
    if len(input_string) >= 2 and input_string[:2] == "Is":
        return input_string
    return "Is" + input_string


inp = raw_input("Enter your String here: ")
checks = form_string(inp)
print(checks)
