fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    wds = line.split()
    for word in wds:
        if word in lst:
            continue
        lst.append(word)
print(sorted(lst))
