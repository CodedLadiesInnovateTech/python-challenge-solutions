# Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values

List = [-2, 5, -10, 5, -4]

for i in range(len(List)):
    for j in range(len(List)):
        if i != j:
            product = List[i] * List[j]
            if product + product > 0:
                print(List[i], List[j])

