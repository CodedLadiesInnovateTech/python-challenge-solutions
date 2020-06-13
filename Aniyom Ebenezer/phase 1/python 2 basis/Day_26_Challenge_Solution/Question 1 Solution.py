"""
Write a Python program to count the number of arguments in a given function.
"""
def count_args(*args):
	return(len(args))
print(count_args())
print(count_args(1))
print(count_args(1, 2))
print(count_args(1, 2, 3))
print(count_args(1, 2, 3, 4))
print(count_args([1, 2, 3, 4]))