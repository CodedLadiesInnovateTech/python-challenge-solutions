# Question 10
# Create a copy of its own source code

print("apple")
print(open(__file__).read())

# ALternative,
#_='_=%r;print (_%%_)';print (_%_) 
