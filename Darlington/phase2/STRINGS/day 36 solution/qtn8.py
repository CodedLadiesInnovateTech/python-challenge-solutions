#program to count characters at same position in a given string 
# (lower and uppercase characters) as in English alphabet.
def count_char_position(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
  
str1 = input("Input a string: ")
print("Number of characters of the said string at same position as in English alphabet:")
print(count_char_position(str1))