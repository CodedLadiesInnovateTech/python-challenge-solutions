"""
Write a Python program to test whether a passed letter is a vowel or not.
 """
string = str(input("Enter a letter "))
vowels = ["a","e","i","o","u"]
if string in vowels:
    print("True")
else:
    print("False")