def sum_diff(x, y):
    sum_no = x + y
    diff_no = abs(x - y)
    boolean = False
    if (x == y) or (sum_no == 5) or (diff_no == 5):
        boolean = True
    return boolean


print (sum_diff(4, 8))
print (sum_diff(4, 9))
print (sum_diff(6, 1))