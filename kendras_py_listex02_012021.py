fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    email = line.split()
    if len(email) < 1 or email[0] != 'From':
        continue
    print(email[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")


