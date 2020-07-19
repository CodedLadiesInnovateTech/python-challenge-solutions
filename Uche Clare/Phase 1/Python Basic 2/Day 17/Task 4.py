#Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers.
import itertools

num ={3, 4, -7, 0, 1, 3, 5, -8, 7}
for i in itertools.combinations(num,3):
    if sum(i) == 0:
        print(f'The unique triplet {i} sums to 0')