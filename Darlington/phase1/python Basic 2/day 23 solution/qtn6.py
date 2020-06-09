#program to check whether a number is "happy" or not.
def is_Happy_num(num):       
    while num != 1:
        
        num = str(num)
        sum_square = 0
        
        for i in num:
            sum_square += int(i) ** 2
        
        num = sum_square
    
    return True

print(is_Happy_num(7))
print(is_Happy_num(932))
