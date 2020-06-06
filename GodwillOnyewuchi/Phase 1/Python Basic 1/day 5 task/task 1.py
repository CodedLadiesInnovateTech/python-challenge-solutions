num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 > num2:
    Bigger = num1
else:
    Bigger = num2

while True:
    if Bigger % num2 == 0 and Bigger % num1 == 0:
        lcm = Bigger
        break
    Bigger = Bigger + 1


print(lcm)
