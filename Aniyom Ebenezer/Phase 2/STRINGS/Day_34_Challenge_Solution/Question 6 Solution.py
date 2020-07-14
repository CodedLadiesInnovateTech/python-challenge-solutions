"""
Write a Python program to find the second most repeated word in a given string.
"""
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    counts_x = sorted(counts.items(), key=lambda kv:kv)
    return counts_x[-2]
print(word_count("both of these by issues fixed by postponding of of annotations."))