import math


# Calculate hypotenuse of a right angled triangle
def calc_hypo(opp, adj):
    opp = math.pow(opp, 2)
    adj = math.pow(adj, 2)
    sum_of_squares = opp + adj
    hyp = math.sqrt(sum_of_squares)
    return hyp


print("To Calculate hypotenuse of a right angled triangle")
opposite = float(input("Enter value for opposite side of triangle"))
adjacent = float(input("Enter value for adjacent side of triangle"))

hypotenuse = round(calc_hypo(opposite, adjacent), 2)
print ("Value for Hypotenuse is " + str(hypotenuse))
