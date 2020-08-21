def pablo (string,number):
    if len(string)>=2 and number > 0:
        a=string[0:2]
        for i in range(number):
            print(a)
    elif len(string) < 2 and number > 0:
        for i in range(number):
            print(string)
    else:
        return print("invalid number of copies")


pablo("Emmanuel",4)
