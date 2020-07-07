'''1. Write a Python program to count the number of arguments in a given function.
Sample Output:
0
1
2
3
4
1'''
def num_of_args(*args):
	return(len(args))
print(num_of_args())
print(num_of_args(1))
print(num_of_args(1, 2))
print(num_of_args(1, 2, 3))
print(num_of_args(1, 2, 3, 4))
print(num_of_args([1, 2, 3, 4]))

#Reference: w3resource