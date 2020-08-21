#program to remove key values pairs from a list of dictionaries.
original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
print("Original List: ")
print(original_list)
new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in original_list]
print("New List: ")
print(new_list)
