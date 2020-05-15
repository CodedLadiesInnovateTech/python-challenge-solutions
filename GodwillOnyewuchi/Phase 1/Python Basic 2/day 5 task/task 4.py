num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

Sum = num1 + num2
if Sum in range(15, 20):
    print(f'Sum = 20')
else:
    print(f'Sum = {Sum}')