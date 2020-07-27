'''10. Write a Python program to insert an element at a specified position into a given list. 
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
After removing an element at the kth position of the said list:
[1, 1, 3, 4, 4, 5, 1] '''

def insert_spec_position(x, n_list, pos):
    return n_list[:pos-1]+[x]+n_list[pos-1:]
n_list = [1,1,2,3,4,4,5,1]
print("Original list:") 
print(n_list)
kth_position = 3
x = 12
result = insert_spec_position(x, n_list, kth_position)
print("\nAfter inserting an element at kth position in the said list:")
print(result)

#Reference: w3resource