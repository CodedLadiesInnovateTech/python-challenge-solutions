'''5. In mathematics, a subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. For example, the sequence (A,B,D) is a subsequence of (A,B,C,D,E,F) obtained after removal of elements C, E, and F. The relation of one sequence being the subsequence of another is a preorder.
The subsequence should not be confused with substring (A,B,C,D) which can be derived from the above string (A,B,C,D,E,F) by deleting substring (E,F). The substring is a refinement of the subsequence.
The list of all subsequences for the word "apple" would be "a", "ap", "al", "ae", "app", "apl", "ape", "ale", "appl", "appe", "aple", "apple", "p", "pp", "pl", "pe", "ppl", "ppe", "ple", "pple", "l", "le", "e", "".
Write a Python program to find the longest word in set of words which is a subsequence of a given string.
Sample Output:
Gren
exercises'''

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

#Reference: w3resource