num1 = int(input("Enter an integer: "))
num2 = int(input("Enter an integer: "))
num3 = int(input("Enter an integer: "))

numbers = [num1, num2, num3]

print(f'In ascending order')
numbers.sort()
print(numbers)

print(f'In descending order,')
numbers.reverse()
print(numbers)
