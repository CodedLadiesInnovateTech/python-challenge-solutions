#Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.
string = '\n It is very important that you conduct a thorough appraisal of yourself in order to know your strengths and weaknesses. This self appraisal is VERY IMPORTANT if you desire to get the kind of job you want. \n If you don’t take time out to properly ascertain your personality and know the kind of job that fits your person, you will face a lot of challenges in your job search. \n Therefore, knowing your strengths and weaknesses is crucial to knowing the way you like to work.'
string1 = string.split()
freq = [string1.count(word) for word in string1 ]


print('String coverted to list', string1)
print()
print("Pairs (words and their frequencies:)\n", (str(list(zip(string1, freq)))))
