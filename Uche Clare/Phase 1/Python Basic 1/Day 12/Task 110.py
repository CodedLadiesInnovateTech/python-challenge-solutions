num = [15, 30, 35, 40, 45, 50, 55, 53, 60, 65, 80, 90, 95, 70]
result = list(filter(lambda x: (x % 15 == 0), num))
print(result)