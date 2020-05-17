def greatest_factor(a,b):
    factors = []
    if a > b:
        print("Enter the smaller number first")
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            factors.append(i)
    return print(f"The greatest common factor of {a} and {b} is", factors[-1])
greatest_factor(6,8)
