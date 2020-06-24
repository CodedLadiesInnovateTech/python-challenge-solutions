#program to count number of substrings from a given string of lowercase
#  alphabets with exactly k distinct (given) characters.
def count_k_dist(str1, k): 
	str_len = len(str1) 
	
	result = 0

	ctr = [0] * 27

	for i in range(0, str_len): 
		dist_ctr = 0

		ctr = [0] * 27

		for j in range(i, str_len): 
			
			if(ctr[ord(str1[j]) - 97] == 0): 
				dist_ctr += 1

			ctr[ord(str1[j]) - 97] += 1

			if(dist_ctr == k): 
				result += 1
			if(dist_ctr > k): 
				break

	return result 

str1 = input("Input a string (lowercase alphabets):")
k = int(input("Input k: "))
print("Number of substrings with exactly", k, "distinct characters : ", end = "") 
print(count_k_dist(str1, k))