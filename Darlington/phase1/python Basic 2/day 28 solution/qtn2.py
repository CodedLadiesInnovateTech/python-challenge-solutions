#program to compute the digit distance between two integers.
def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))
print(digit_distance_nums(123, 256))
print(digit_distance_nums(23, 56))
print(digit_distance_nums(1, 2))
print(digit_distance_nums(24232, 45645))