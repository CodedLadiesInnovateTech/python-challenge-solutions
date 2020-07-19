def number_test(n):
    return((abs(1000-n) <=100) or (abs(2000-n) <=100))
print(number_test(1000))
print(number_test(900))