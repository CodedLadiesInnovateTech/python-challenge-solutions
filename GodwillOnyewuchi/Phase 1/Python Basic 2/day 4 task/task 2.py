lists = [2, 3, 4, 5, 6, 4, 4, 5, 8]
count = 0
for i in lists:
    if i == 4:
        count += 1
print(f'Number 4 appeared {count} times')