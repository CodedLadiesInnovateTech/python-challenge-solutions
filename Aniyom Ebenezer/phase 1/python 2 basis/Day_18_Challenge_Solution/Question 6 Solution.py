"""
Write a Python program to get the third side of right angled triangle from two given sides.
"""
def get_third_side(opp, adj, hyp):
    if opp == str("x"):
        return("oppisite side = ", round(((hyp)**2 - (adj)**2)**0.5, 2))
    elif adj == str("x"):
        return("Adjacent side = ", round(((hyp)**2 - (opp)**2)**0.5,2))
    elif hyp == str("x"):
        return("Hypothenus side = ", round(((opp)**2 + (adj)**2)**0.5, 2))
    else:
        return("All sides provided")
print(get_third_side(2,3,"x"))
print(get_third_side(4,"x", 5))
print(get_third_side("x", 6, 7))
print(get_third_side(1,2,3))