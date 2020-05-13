def calc_sum(param):
    param = [x.strip(' ') for x in param]
    message = "Let there be more than three numbers"
    sum_up = 0
    if len(param) < 3:
        return message
    for x in param:
        sum_up += int(x)
    message = "Sum of number in List is: "
    if param[0] == param[1] == param[2]:
        sum_up = sum_up * 3
    return message + " " + str(sum_up)


input_seq = list(str(raw_input("Enter numbers to sum up separated by comma: ")).split(','))
print(input_seq)

print (calc_sum(input_seq))


