"""
Write a Python program to find heights of the top three buillding in descending order from eight
given building
"""
print("Input the heights of eight buildings: ")
l = [int(input())for i in range(8)] 
print("Heights of the top three buildings: ")
l=sorted(l)
print(*l[:4:-1], sep='\n')

# reference: w3resource