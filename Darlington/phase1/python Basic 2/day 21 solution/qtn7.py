#program which reads a text (only alphabetical characters and spaces.) and prints two words. 
# The first one is the word which is arise most frequently in the text. 
# The second one is the word which has the maximum number of letters.
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