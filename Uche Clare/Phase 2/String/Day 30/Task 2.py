#Write a Python program to count the occurrences of each word in a given sentence. 
sentence = 'A good tactic is to say that you always prioritise the most important and urgent tasks to the top of the pile. When that doesn’t work, say that you enlist colleagues to help or check whether the deadline can be moved. As a final option, you can say that you simply get on with the work and stay late to get everything done.'
sentence = sentence.split()
print(sentence)
occurrences = [sentence.count(occ) for occ in sentence]
print()
print('The occurances of the sentence above is given as:\n', str(set(zip(sentence, occurrences))))