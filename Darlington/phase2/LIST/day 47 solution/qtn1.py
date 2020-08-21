# program to extract a given number of randomly selected elements from a given list.
import random
def random_select_nums(n_list, n):
        return random.sample(n_list, n)
n_list = [1,1,2,3,4,4,5,1]
print("Original list:") 
print(n_list)
selec_nums = 3
result = random_select_nums(n_list, selec_nums)
print("\nSelected 3 random numbers of the above list:")
print(result) 
print(n_list)
selec_nums1 = 5
result1 = random_select_nums(n_list, selec_nums1)
print("\nSelected 5 random numbers of the above list:")