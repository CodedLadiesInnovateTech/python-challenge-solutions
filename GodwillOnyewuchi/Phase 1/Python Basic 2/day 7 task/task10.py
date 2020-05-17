import math
opposite = int(input("Enter the opposite side: "))
adjacent = int(input("Enter the opposite side: "))

hypotenuse = math.sqrt(math.pow(opposite, 2) + math.pow(adjacent, 2))

print(f'hypotenuse = {hypotenuse}')