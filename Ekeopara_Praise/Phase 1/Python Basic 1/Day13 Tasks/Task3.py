'''3. Write a Python program to input a number, if it is not a number generate an error message.'''

number = input("Enter a number: ")
try:
    int(number)
    print(f"{number} is a number.")
except:
    print(f"Error: {number} is not a number!")