#program to check if a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

c = {4: 20,6: 24, 7: 45}
def is_word_absent(y):
    if y in c:
        print('the word is present')
    else:
        print('the word is absent')
is_word_absent(6)
is_word_absent(8)            
