#Find the longest word in set of words which is a subsequence of a given string
def longest_word_sequence(s, d):
	long_word = ""
	
	for word in d: 
		temp_word = ''	
		j = 0
		for letter in word: 

			for i in range(j, len(s)): 

				if letter == s[i]: 
					temp_word += letter 
					j = i                  
					break
				else:				
					continue        

		if (temp_word) == word and len(long_word) < len(temp_word):
			long_word = temp_word

		else:
			continue
	return long_word


print(longest_word_sequence("Green", {"Gn", "Gren", "ree", "en"}))
print(longest_word_sequence("pythonexercises", {"py", "ex", "exercises"}))