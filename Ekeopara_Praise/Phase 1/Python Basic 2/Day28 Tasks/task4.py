'''4. Write a Python program to print letters from the English alphabet from a-z and A-Z.
Sample Output:
Alphabet from a-z:
a b c d e f g h i j k l m n o p q r s t u v w x y z
Alphabet from A-Z:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'''

def lowercaseAlphabets(): 
    for c in range(97, 123): 
        print(chr(c), end = " "); 
def uppercaseAlphabets():
    for c in range(65, 91): 
        print(chr(c), end = " "); 

print("Alphabet from A-Z:"); 
uppercaseAlphabets(); 
  
print("\nAlphabet from a-z: "); 
lowercaseAlphabets();
uppercaseAlphabets();
  