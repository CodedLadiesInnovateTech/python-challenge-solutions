def even_odd ():
    number = float(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is an even number")
    elif number % 2 == 1:
        print(f"{number} is an odd number")
    else:
        print(f"{number} is neither even nor odd")
even_odd()