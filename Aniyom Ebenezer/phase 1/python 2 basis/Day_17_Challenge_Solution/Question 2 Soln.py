"""Write a Python program to create all possible strings by using 'a','e','i','o','u'.
use the characters exactly"""

import random
char_list = ['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))