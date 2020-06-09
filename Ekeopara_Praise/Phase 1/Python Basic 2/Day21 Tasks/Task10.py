'''10. Write a Python program to replace a string "Python" with "Java" and "Java" with "Python" in a given string.
Input:
English letters (including single byte alphanumeric characters, blanks, symbols) are given on one line. The length of the input character string is 1000 or less.
Input a text with two words 'Python' and 'Java'
Python is popular than Java
Java is popular than Python'''

print("Input a text with two words 'Python' and 'Java'")
text = input().split()
for i in range(len(text)):
    if "Python" in text[i]:n = text[i].index("Python");text[i] = text[i][:n] + "Java" + text[i][n + 6:]
    elif "Java" in text[i]:n = text[i].index("Java");text[i] = text[i][:n] + "Python" + text[i][n + 4:]
print(*text)

#Reference: w3resource
