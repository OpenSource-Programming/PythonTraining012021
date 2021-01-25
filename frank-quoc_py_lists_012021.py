# Exercise 8.4
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    curr_lst = line.split()
    for word in curr_lst:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)

# Exercise 8.5
fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] == "From":
        count += 1
        print(words[1])
print("There were", count, "lines in the file with From as the first word")
