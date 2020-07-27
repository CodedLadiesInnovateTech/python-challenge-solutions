# Python program to get numbers divisible by fifteen from a list using an anonymous function

def divisibleby15(lists):
    newList = []
    for i in lists:
        if i % 15 == 0:
            newList.append(i)
    return newList

print(divisibleby15([23, 56, 12, 15, 45, 23, 70, 678, 90]))