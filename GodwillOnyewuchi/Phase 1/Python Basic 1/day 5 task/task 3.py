num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

Sum = num1 + num2 + num3
if num1 == num2 or num1 == num3 or num2 == num3:
    print(f'Sum = 0')
else:
    print(f'Sum = {Sum}')

