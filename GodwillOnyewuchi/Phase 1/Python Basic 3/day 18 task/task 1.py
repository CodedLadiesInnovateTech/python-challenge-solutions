# Write a Python program to check the sum of three elements (each from an array) from three arrays is
# equal to a target value. Print all those three-element combinations

X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]

Combinations = []

for i in range(len(X)):
    for j in range(len(Y)):
        for k in range(len(Z)):
            if X[i] + Y[j] + Z[k] == 70:
                Combinations.append([X[i], Y[j], Z[k]])

for i in range(len(Combinations)):
    for j in range(len(Combinations)):
        if i == j:
            Combinations.pop(j)
print(Combinations)