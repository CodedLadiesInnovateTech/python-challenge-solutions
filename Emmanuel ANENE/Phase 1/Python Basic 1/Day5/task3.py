num1 = int(input("Enter a number: "))
num2 = int(input("Enter a another number: "))
num3 = int(input("Enter a final number: "))

def add(num1, num2, num3):
    if num1 == num2 or num2 == num3 or num1 == num3:
        tot = 0
        return tot
    else:
        tot = num1 + num2 + num3
        return tot

print(add(num1, num2, num3))