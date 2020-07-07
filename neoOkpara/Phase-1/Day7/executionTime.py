from __future__ import print_function

import time


def sum_of_n_numbers(num):
    start_time = time.time()
    full_sum = 0
    for i in range(1, num + 1):
        full_sum = full_sum + i
    end_time = time.time()
    return full_sum, end_time - start_time


n = 43
print("\nTime to sum of 1 to ", n, " and required time to calculate is :", sum_of_n_numbers(n))
