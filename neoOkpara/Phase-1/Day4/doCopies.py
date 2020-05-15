def do_copies(string, n):
    copies = ""
    i = 2  # no_of_characters to slice
    if len(string) < 2:  # any number less than 2 and is non -ve will only be 1
        i = len(string)
    new_string = string[:i]
    for x in range(n):
        copies += new_string
    return copies


print (do_copies("messiah", 4))
print (do_copies("d", 6))
