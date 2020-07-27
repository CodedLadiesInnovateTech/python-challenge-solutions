# Write a Python program to create a sequence where the first four members of the sequence are equal to one,
# and each successive term of the sequence is equal to the sum
# of the four previous ones. Find the Nth member of the sequence

Sequence = [1, 1, 1, 1]
sum = 0
for i in range(10):
    for j in Sequence:
        sum += j

    Sequence.append(sum)

print(Sequence)
