# Exercise 7.1
# fh = open("mbox-short.txt")
# for lx in fh:
#     ly = lx.rstrip()
#     print(ly.upper())

# Exercise 7.2
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
tot = 0
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        num = float(line.strip("X-DSPAM-Confidence:"))
        count += 1
        tot += num
avg = tot / count
print("Average spam confidence:", avg)