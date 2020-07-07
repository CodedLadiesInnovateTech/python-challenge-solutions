# Write a Python program to get all strobogrammatic numbers that are of length n

# reference https://github.com/keon/algorithms/blob/master/math/generate_strobogrammtic.py
def gen_strobogrammatic(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = helper(n, n)
    return result


def helper(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = helper(n-2, length)
    result = []
    for middle in middles:
        if n != length:
            result.append("0" + middle + "0")
        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
    return result


print(f'n = 2:  {gen_strobogrammatic(2)}')
print(f'n = 3:  {gen_strobogrammatic(3)}')