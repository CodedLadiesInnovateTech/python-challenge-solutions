"""
Write a Python program to compute the digit distance between two integers.
The digit distance between two numbers is the absolute value of the difference of those numbers.
For example, the distance between 3 and −3 on the number line given by the |3 – (−3) | = |3 + 3 | = 6 units
Digit distance of 123 and 256 is
Since |1 - 2| + |2 - 5| + |3 - 6| = 1 + 3 + 3 = 7
"""
def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))
print(digit_distance_nums(123, 256))
print(digit_distance_nums(23, 56))
print(digit_distance_nums(1, 2))
print(digit_distance_nums(24232, 45645))