#Python program to clear the screen or terminal.
import os
os.system('cls' if os.name == 'nt' else 'clear')

