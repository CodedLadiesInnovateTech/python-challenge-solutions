"""
Write a Python program to split a list every Nth element.
"""
C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
def list_slices(S, step):
    return [S[i::step] for i in range(step)]
print(list_slices(C, 3))