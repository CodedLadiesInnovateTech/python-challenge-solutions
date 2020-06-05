""" Write a Python program to print a long text to print a long text, convert the string to a list and print all the words
and their frequencies"""
string_text = """
Hey over there, I am Aniyom Eben, I am grateful being a part of this Challenge for it has really revealed to me more ways
of solving  problems using Python
"""
string_list = string_text.split()

string_freq = [string_text.count(n) for n in string_list]

print("String: \n{}".format(string_text))
print("List: \n{}".format(str(string_list)))
print("Piars (words and frequencies: \n{}".format(str(list(zip(string_list, string_freq)))))