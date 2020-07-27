# Write a Python program to get all possible two digit letter combinations from a digit (1 to 9) string

digits = '33'

string_maps = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z"
}
result = [""]
for i in digits:
    combination = []
    for j in result:
        for char in string_maps[i]:
            combination.append(j + char)
        result = combination

print(result)