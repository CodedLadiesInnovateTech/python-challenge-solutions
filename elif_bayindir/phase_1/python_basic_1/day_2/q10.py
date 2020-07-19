# Question 10

# Accept an integer (n) and compute the value of n+nn+nnn

n = int(input("Enter an integer: "))
new_num = n + int(str(n) * 2) + int(str(n) * 3)
print("Expected Result: ", new_num)

# Alternative method,
# new_num = n + int("%s%s" % (n, n)) + int("%s%s%s" % (n, n, n))

