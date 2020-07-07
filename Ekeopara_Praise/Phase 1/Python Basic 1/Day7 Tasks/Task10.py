'''10. Write a Python program to calculate the hypotenuse of a right angled triangle'''

def hyp(adj, oppo):
    hypo = (adj**2 + oppo**2)**0.5
    return f"The hypotenuse is: {hypo}"

print(hyp(2, 3))