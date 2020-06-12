#program to reverse only the vowels of a given string.
def reverse_vowels(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
print(reverse_vowels("w3resource"))
print(reverse_vowels("Python"))
print(reverse_vowels("Perl"))
print(reverse_vowels("USA"))