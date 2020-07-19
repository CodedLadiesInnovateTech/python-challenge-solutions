num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

def addVal(num1, num2):
    tot = num1 + num2     
    if tot >= 15 and tot <= 20:
        tot = 20
        return "Forced total = {}".format(tot)
    else:
        return "Total = {}".format(tot)

print(addVal(num1, num2))