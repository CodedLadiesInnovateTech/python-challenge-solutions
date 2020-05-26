from __future__ import print_function


def check_greater_no(num, stored_nums=[]):
    # if stored_nums.__contains__(num):
    #     print("List contains number:", num)
    # else:
    #     print("List does not contain:", num)
    for i in stored_nums:
        if i < num:
            print("Given Number {0} is greater than {1} of the list".format(num, i))


stored_numbers = [34, 65, 28, 89]
check_greater_no(55, stored_numbers)

print(all(x > 23 for x in stored_numbers))
