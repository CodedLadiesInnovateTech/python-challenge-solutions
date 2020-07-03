#program to find the index of a given string at which a given substring starts.
#If the substring is not found in the given string return 'Not found'.
def find_Index(str1, pos):
    if len(pos) > len(str1):
        return 'Not found'

    for i in range(len(str1)):

        for j in range(len(pos)):

            if str1[i + j] == pos[j] and j == len(pos) - 1:
                return i
                
            elif str1[i + j] != pos[j]:
                break

    return 'Not found'
print(find_Index("Python Exercises", "Ex"))
print(find_Index("Python Exercises", "yt"))
print(find_Index("Python Exercises", "PY"))
