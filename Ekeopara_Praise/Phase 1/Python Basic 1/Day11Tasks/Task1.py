'''1. Write a Python program to swap two variables.'''

def swap(vr1, vr2):
    vr1, vr2 = vr2, vr1
    return vr1, vr2

print(swap(20, 400))
