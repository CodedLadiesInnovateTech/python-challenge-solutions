# program to find smallest window that contains all characters of a given string.
from collections import defaultdict   

def find_sub_string(str): 
    str_len = len(str) 
      
    # Count all distinct characters. 
    dist_count_char = len(set([x for x in str])) 
  
    ctr, start_pos, start_pos_index, min_len = 0, 0, -1, 9999999999
    curr_count = defaultdict(lambda: 0) 
    for i in range(str_len): 
        curr_count[str[i]] += 1
 
        if curr_count[str[i]] == 1: 
            ctr += 1
  
        if ctr == dist_count_char: 
            while curr_count[str[start_pos]] > 1: 
                if curr_count[str[start_pos]] > 1: 
                    curr_count[str[start_pos]] -= 1
                start_pos += 1
  
            len_window = i - start_pos + 1
            if min_len > len_window: 
                min_len = len_window 
                start_pos_index = start_pos 
    return str[start_pos_index: start_pos_index + min_len] 
      
str1 = "asdaewsqgtwwsa"
print("Original Strings:\n",str1)
print("\nSmallest window that contains all characters of the said string:")
print(find_sub_string(str1)) 