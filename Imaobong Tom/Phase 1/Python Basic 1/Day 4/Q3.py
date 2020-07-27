def string_copy(string, n):
    if n <= 0:
        print ("Enter a valid number")
    result = ""
    for i in range(n):
        if len(string)>= 2 and n > 0:
            result = result + string[0:2]
        elif len(string) < 2:
            result = result + string
    return(result)
print(string_copy("blue",3))

