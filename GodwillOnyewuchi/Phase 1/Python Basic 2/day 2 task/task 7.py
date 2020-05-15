
filename = input("Enter a filename with extension: ")

for i in range(len(filename)):
    if filename[i] == ".":
        extension = filename[(i+1):]
        break;

print(f'Sample filename: {filename} ')
print(f'Output: {extension}')