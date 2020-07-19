#program to generate groups of five consecutive numbers in a list.
l = [[5*i + j for j in range(1,6)] for i in range(5)]
print(l)