# Write a Python program to get the third side of right angled triangle from two given sides

import math

def pythagoras(opposite_side, adjacent_side, hypotenuse):
    if opposite_side == str("x"):
        opposite_side = math.sqrt(math.pow(hypotenuse, 2) - math.pow(adjacent_side, 2))
        return f'Opposite = {opposite_side}'
    elif adjacent_side == str("x"):
        adjacent_side = math.sqrt(math.pow(hypotenuse, 2) - math.pow(opposite_side, 2))
        return f'adjacent = {adjacent_side}'
    elif hypotenuse == str("x"):
        hypotenuse = math.sqrt(math.pow(opposite_side, 2) + math.pow(adjacent_side, 2))
        return f'hypotenuse = {hypotenuse}'
    else:
        return "You know the answer!"


print(pythagoras(3, 4, 'x'))
