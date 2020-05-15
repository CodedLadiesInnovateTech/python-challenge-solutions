def join_string(lists):
    message = ""
    for x in lists:
        message += str(x)
    return message


group = [34, 56, 78, 89]
string_list = ["I ", "am ", "gradually ", "understanding Python", ". Hurray"]

print (join_string(group))
print (join_string(string_list))
