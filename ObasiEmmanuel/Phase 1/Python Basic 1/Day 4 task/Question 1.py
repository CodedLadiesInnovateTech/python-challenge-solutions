def number_checker ():
    number = float(input("Enter number: "))
    if number % 2 == 0 :
        return print("number is even")
    elif number % 2 == 1:
        return print("number is odd")
    else:
        return print("number is neither even nor odd, please insert an integer number")


number_checker()