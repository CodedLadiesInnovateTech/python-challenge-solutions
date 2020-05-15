def check_values(group, value):
    for x in group:
        if x == value:
            return True
    return False


print (check_values([34, 56, 77], 22))
print (check_values([34, 56, 77], 34))
