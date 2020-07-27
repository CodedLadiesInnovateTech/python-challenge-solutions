#program to print a given N by M matrix of numbers line by line in forward >
#  backwards > forward >... order.
 def print_matrix(nums):
    flag = True 
    
    for line in nums:

        if flag == True: 
            i = 0
            while i < len(line):
                print(line[i])
                i += 1
            flag = False

        else: 
            i = -1
            while i > -1 * len(line) - 1:
                print(line[i])
                i = i - 1
            flag = True
print_matrix([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [0, 6, 2, 8],
              [2, 3, 0, 2]])