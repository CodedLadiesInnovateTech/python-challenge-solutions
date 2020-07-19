# Question 6
# Get the path and name of the file that is currently executing
	
import os

print("Path of the file that is currently executing :",os.path.realpath(__file__))

# Alternative,
	
""" from pathlib import Path

print("Path of the file that is currently executing :", Path(__file__).resolve()) """
