def sum_numbers(a,b,c):
    sum = a + b + c
    if a==b or a==c or b==c:
        sum = 0
    return sum
print(sum_numbers(3,3,5))
