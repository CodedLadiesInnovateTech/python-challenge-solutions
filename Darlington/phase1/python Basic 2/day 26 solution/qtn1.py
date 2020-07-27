# program to count the number of arguments in a given function.
def num_of_args(*args):
	return(len(args))
print(num_of_args())
print(num_of_args(1))
print(num_of_args(1, 2))
print(num_of_args(1, 2, 3))
print(num_of_args(1, 2, 3, 4))
print(num_of_args([1, 2, 3, 4]))