'''1. Write a Python program to find the difference between the largest integer and the smallest integer which are created by 8 numbers from 0 to 9. The number that can be rearranged shall start with 0 as in 00135668.
Input:
Input an integer created by 8 numbers from 0 to 9.:
2345
Difference between the largest and the smallest integer from the given integer:
3087'''

print("Input an integer created by 8 numbers from 0 to 9.:")
num = list(input())
print("Difference between the largest and the smallest integer from the given integer:")
print(int("".join(sorted(num,reverse=True))) - int("".join(sorted(num))))

#Reference: w3resource