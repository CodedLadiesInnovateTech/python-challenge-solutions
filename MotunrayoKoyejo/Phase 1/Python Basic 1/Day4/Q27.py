def concat(elements):
    result = ''
    for element in elements:
        result +=str(element)
    return result


print(concat([3,4,5,6]))