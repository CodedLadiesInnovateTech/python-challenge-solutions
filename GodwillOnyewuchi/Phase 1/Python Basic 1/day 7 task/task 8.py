
print("Calculate the sum of n positive integers")
num = int(input("Enter an integer: "))
output = 0
for n in range(num + 1):
    output += ((n * (n + 1)) / 2)

print(output)