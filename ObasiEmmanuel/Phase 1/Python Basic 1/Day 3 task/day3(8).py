def calculator():
    a=float(input("enter first number"))
    b=float(input("enter second number"))
    c=float(input("enter third number"))
    if a==b==c:
        sum=float(3*(a+b+c))
        return sum
        print(sum)
    else:
            sum=a+b+c
            return sum
            print(sum)
print(calculator())


