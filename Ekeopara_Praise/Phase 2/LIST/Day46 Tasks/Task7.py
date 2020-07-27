'''7. Write a Python program to decode a run-length encoded given list. 
Original encoded list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Decode a run-length encoded said list:
[1, 1, 2, 3, 4, 4, 5, 1] '''

def decode(alist):
    def aux(g):
        if isinstance(g, list):
            return [(g[1], range(g[0]))]
        else:
            return [(g, [0])]
    return [x for g in alist for x, R in aux(g) for i in R]
n_list = [[2, 1], 2, 3, [2, 4], 5, 1]
print("Original encoded list:") 
print(n_list)
print("\nDecode a run-length encoded said list:")
print(decode(n_list))

#Reference: w3resource