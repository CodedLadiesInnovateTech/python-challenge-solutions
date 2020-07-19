def substring(string, b):
    cop = 2
    if cop > len(string):
        cop = len(string)
    substr = string[:cop]

    result = ""
    for i in range(b):
        result = result + substr
    return result

    print(substring('madam', 2))