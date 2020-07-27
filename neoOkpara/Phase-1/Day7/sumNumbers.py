def sum_of_n_numbers(num):
    full_sum = 0
    for i in range(1, num + 1):
        full_sum = full_sum + i
    return full_sum


print (sum_of_n_numbers(5))
