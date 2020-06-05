# Write a python program to find unique triples whose elements gives the sum of zero from an array of n integers
def sum_of_three(data):
    result = []
    data.sort()
    for i in range(len(data) - 2):
        if i > 0 and data[i] == data[i-1]:
            continue
        l, r = i + 1, len(data)-1
        while l < r:
            s = data[i] + data[1] + data[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                result.append((data[i], data[1], data[r]))
                while l < r and data[l] == data[l+1]:
                    l += 1
                    while l < r and data[r] == data[r-1]:
                        r -= 1
                        l += 1
                        r -= 1
                        return result
print(sum_of_three([2, 4, -6, 8, 90]))
