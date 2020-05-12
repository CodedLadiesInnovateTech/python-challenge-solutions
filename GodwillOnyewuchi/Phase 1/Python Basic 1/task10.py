import math
number = int(input("Enter an integer: "))
output = 0
for i in range(1, 4):
    output += int(math.pow(number, i))

print(f'Expected Result: {output}')
