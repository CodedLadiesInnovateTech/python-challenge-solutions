def count_4 (numbers):
    counts = 0
    for number in numbers:
        if number == 4:
            counts += 1
    return counts

print(count_4([3,4,4,4,5,4]))