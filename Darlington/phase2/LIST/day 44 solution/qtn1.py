# program to split a list every Nth element.
C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
def list_slice(S, step):
    return [S[i::step] for i in range(step)]
print(list_slice(C,3))