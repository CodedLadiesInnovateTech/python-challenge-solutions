#program concatenate
def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([4, 6, 2, 0, 34, 8]))