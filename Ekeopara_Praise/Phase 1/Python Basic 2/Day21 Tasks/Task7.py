'''7. Write a Python program which reads a text (only alphabetical characters and spaces.) 
and prints two words. The first one is the word which is arise most frequently in the text.
 The second one is the word which has the maximum number of letters.
Note: A word is a sequence of letters which is separated by the spaces.
Input:
A text is given in a line with following condition:
a. The number of letters in the text is less than or equal to 1000.
b. The number of letters in a word is less than or equal to 32.
c. There is only one word which is arise most frequently in given text.
d. There is only one word which has the maximum number of letters in given text.
Input text: Thank you for your comment and your participation.
Output: your participation.'''

import collections
print("Input a text in a line.")
text_list = list(map(str, input().split()))
sc = collections.Counter(text_list)
common_word = sc.most_common()[0][0]
max_char = ""
for s in text_list:
    if len(max_char) < len(s):
        max_char = s
print("\nMost frequent text and the word which has the maximum number of letters.")
print(common_word, max_char)

#Reference: w3resource