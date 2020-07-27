num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

def truthy(num1, num2):
    tot = num1 + num2     
    if num1 == num2 or abs(num1 + num2) == 5 or abs(num1 - num2) == 5:
        return True
    else:
        return False
    
print(truthy(num1, num2))