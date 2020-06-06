text = input("Enter a string of text: ")	
checkIs = text[0:2]
Isword = ['is', 'Is', 'IS']	
if checkIs in Isword:	

    print(text)	
else:	
    texts = f'Is {text}'	
    print(texts)