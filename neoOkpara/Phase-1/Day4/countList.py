def count_list(lists):
    count = 0
    for num in lists:
        if num == 4:
            count += 1
    return count


new_list = [34, 4, 56, 4, 22]
print (count_list(new_list))
