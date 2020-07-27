def join_strings(num):
    list_string = []
    for i in range(num):
        sample = str(raw_input("Add a string you wish to concatenate: \n"))
        list_string.append(sample)

    joined_string = ' '.join(sorted(list_string))
    print(joined_string)


n = int(input("Enter the number of strings to concatenate: \n"))
join_strings(n)
