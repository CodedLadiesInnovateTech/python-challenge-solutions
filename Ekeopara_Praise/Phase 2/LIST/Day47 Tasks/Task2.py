'''2. Write a Python program to generate the combinations of n distinct objects taken from the elements
 of a given list. 
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct 
objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]
'''

def combination(n, n_list):
    if n<=0:
        yield []
        return
    for i in range(len(n_list)):
        c_num = n_list[i:i+1]
        for a_num in combination(n-1, n_list[i+1:]):
            yield c_num + a_num
n_list = [1,2,3,4,5,6,7,8,9]
print("Original list:") 
print(n_list)
n = 2
result = combination(n, n_list)
print("\nCombinations of",n,"distinct objects:")
for e in result:
     print(e)

#Reference: w3resource